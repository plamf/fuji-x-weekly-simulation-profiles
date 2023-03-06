import os
import xml.etree.ElementTree as ET
import sys

master_template_path = sys.argv[1]
receiving_templates_folder = os.getcwd()

# Create subfolder for converted files
converted_folder = os.path.join(receiving_templates_folder, "converted")
os.makedirs(converted_folder, exist_ok=True)

# Parse master template
master_tree = ET.parse(master_template_path)
master_root = master_tree.getroot()

# Loop through receiving templates folder
for filename in os.listdir(receiving_templates_folder):
    if filename.endswith(".FP1"):
        # read the receiving template and extract the comments
        with open(os.path.join(receiving_templates_folder, filename), "r") as f:
            content = f.read()
            comments = content.splitlines()[1:3]

        receiving_template_path = os.path.join(receiving_templates_folder, filename)
        receiving_tree = ET.parse(receiving_template_path)
        receiving_root = receiving_tree.getroot()

        # Update receiving template with values from master template
        receiving_root.set("application", master_root.get("application"))
        receiving_root.set("version", master_root.get("version"))
        property_group = receiving_root.find("./PropertyGroup")
        property_group.set("device", master_root.find("./PropertyGroup").get("device"))
        property_group.set("version", master_root.find("./PropertyGroup").get("version"))
        tags_to_change = ["SerialNumber", "TetherRAWConditonCode", "Editable", "SourceFileName", "Fileerror", "RotationAngle", "StructVer", "IOPCode", "ShootingCondition", "FileType", "ImageSize", "ImageQuality", "LensModulationOpt", "ColorSpace"]

        for child in property_group:
            tag = child.tag
            if tag in tags_to_change:
                value = master_root.find("./PropertyGroup/{}".format(tag)).text
                child.text = value

        # Save converted file with comments
        converted_path = os.path.join(converted_folder, filename)
        with open(converted_path, "wb") as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>'.encode("utf-8"))
            # Write comments
            f.write("\n{}\n{}\n".format(comments[0], comments[1]).encode("utf-8"))
            # Write updated XML content
            receiving_tree.write(f, encoding="utf-8")
    
print("Done converting!")
