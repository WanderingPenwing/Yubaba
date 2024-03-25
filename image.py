import ffmpeg

def image_convert(input_list, output_folder, output_extension):
    for input_file in input_list:
        input_file = input_file.replace("\\", "/")
        input_name = input_file.split('.')
        
        input_path = input_name[0].split("/")
        
        if output_folder != "" and output_folder[-1] != "/":
            output_folder += "/"
        
        output_file = output_folder + input_path[-1] + "." + output_extension

        print("------------------------------------")
        print(input_file, " -> ", output_file)
        ffmpeg.input(input_file).output(output_file, vframes=1).run()

if __name__ == '__main__':
    image_convert(['D:\Docs\@PAUL\ICAM\I4\Hackhaton\Yubaba\images\crazy squirrel.jpg'], '', 'png')
    image_convert(['D:\Docs\@PAUL\ICAM\I4\Hackhaton\Yubaba\images\crazy squirrel.png'], 'converted_images', 'jpeg')