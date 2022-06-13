def cast_field_name(fields_to_convert):
    items_to_delete_and_add = []
    items_to_add = []
    items_to_calculate = []
    calculation_fails = []
    for feature_class in fields_to_convert:
        
        for item in feature_class["fields"]:
            field_key = list(item.keys())[0]
            items_to_delete_and_add.append(field_key)
            items_to_add.append(item[field_key])
            items_to_calculate.append(item[field_key][0])
        print("Field affected: {}".format(items_to_delete_and_add))

            
        fc_path = os.path.join(feature_class["gdb"], feature_class["fc"])
        arcpy.management.AddFields(fc_path, items_to_add)
        for calc_field, old_field in zip(items_to_calculate, items_to_delete_and_add):
            try:
                arcpy.CalculateField_management(fc_path, calc_field, "!{}!".format(old_field), "PYTHON3")
                print("Calculated field for: {}".format(calc_field))
                arcpy.management.DeleteField(fc_path, old_field)
                print("Deleted field: {}".format(old_field))
                arcpy.AlterField_management(fc_path, calc_field, old_field, old_field)
                print("Altered new name to old name: {}".format(calc_field))

            except Exception as e:
                print("FAILED: {}. Not deleting this field when operation completed.".format(old_field))
                print("Failed due to {}".format(e))
                calculation_fails.append(old_field)
                items_to_delete_and_add.remove(old_field)
                
            
    

fields_to_convert_main_table = [
    {
        "gdb" : r"C:\Users\ssellars\Documents\CJOC\SAR\SAR_ETL_V3\Data\SAR_OUTPUT.gdb",
        "fc" : "SARMIS_DATA_COLLECTION",
        "fields" : [
            {"squadron":["squadron_dup", "TEXT"]},
            {"stooddown_time":["stooddown_time_dup", "DATE"]},
            {"red":["red_dup", "LONG"]},
            {"yellow":["yellow_dup", "LONG"]},
            {"green":["green_dup", "LONG"]},
            {"blue":["blue_dup", "LONG"]},
            {"white":["white_dup", "LONG"]},
            {"gray":["gray_dup", "LONG"]},
            {"gray":["gray_dup", "LONG"]},
            {"apprv1_date":["apprv1_date_dup", "DATE"]},
            {"apprv2_date":["apprv2_date_dup", "DATE"]},
            {"apprv3_date":["apprv3_date_dup", "DATE"]},
            {"apprv4_date":["apprv4_date_dup", "DATE"]},
        ]}
]

fields_to_convert_gp_legs = [
    {
        "gdb" : r"C:\Users\ssellars\Documents\CJOC\SAR\SAR_ETL_V3\Data\SAR_OUTPUT.gdb",
        "fc" : "travel_leg_gp",
        "fields" : [
            {"takeoff_time":["takeoff_time_dup", "DATE"]},
            {"on_scene_time":["on_scene_time_dup", "DATE"]},
            {"off_scene_time":["off_scene_time_dup", "DATE"]},
            {"land_time":["land_time_dup", "DATE"]}
        ]}
]

fields_to_convert_st_list = [
    {
        "gdb" : r"C:\Users\ssellars\Documents\CJOC\SAR\SAR_ETL_V3\Data\SAR_OUTPUT.gdb",
        "fc" : "st_list",
        "fields" : [
            {"st_use_no":["st_use_no_dup", "LONG"]},
        ]}
]


eq_used_mis_list = [
    {
        "gdb" : r"C:\Users\ssellars\Documents\CJOC\SAR\SAR_ETL_V3\Data\SAR_OUTPUT.gdb",
        "fc" : "eq_used_mis_list",
        "fields" : [
            {"eq_used_mis_no":["eq_used_mis_no_dup", "LONG"]},
        ]}
]


cast_field_name(fields_to_convert_main_table)
cast_field_name(fields_to_convert_gp_legs)
cast_field_name(fields_to_convert_st_list)
