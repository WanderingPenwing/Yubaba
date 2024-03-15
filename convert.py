import ffmpeg
# (
#     ffmpeg
#     .input('input.mp4')
#     .hflip()
#     .output('output.mp4')
#     .run()
# )

type_conv = {
    'IMAGE' : ['jpeg','png'],
	'VIDEO' : ['mp4'],
	'AUDIO' : ['mp3','wav']
}
def find_file_name(input_path):
	name = ''
	ext = ''
	dot = False
	slash = False
	for _ in range(-1,-len(input_path)-1,-1):
		L = input_path[_]
		if L == '.':
			dot = True
			continue
		if L == '/':
			slash = True
		
		if not dot:
			ext += L
		
		if dot and not slash:
			name += L
	return name[::-1], ext[::-1]

def convert(input_path, output_path, ex_from='', ex_to='') :
	
	file_type = None
	for key in type_conv:
		for ext in type_conv[key]:
			if ext == ex_from:
				print('You are trying to convert a '+ key)
				file_type = key
				break
		if file_type != None:
			break
	
	print(find_file_name(input_path))

	ffmpeg.input('input_path')
#     .output('')
#     .run()


if __name__ == '__main__':
	convert('kijuytrezhgfd/test.webp', 'images/test.jpg')