import ffmpeg
# (
#     ffmpeg
#     .input('input.mp4')
#     .hflip()
#     .output('output.mp4')
#     .run()
# )

TYPE = {
    'IMAGE' : ['jpeg','jpg','png','webp'],
	'VIDEO' : ['mp4'],
	'AUDIO' : ['mp3','wav']
}


def find_file_name(input_path):
	name = ''
	ext = ''
	parent = ''

	dot = False
	slash = False
	for _ in range(-1,-len(input_path)-1,-1):
		L = input_path[_]
		if L == '.' and not dot:
			dot = True
			continue
		if L == '/':
			slash = True
		
		if not dot:
			ext += L
		elif dot and not slash:
			name += L
		elif slash:
			parent += L
	return parent [::-1], name[::-1], ext[::-1]


def convert(input_path, ex_to=str,  output_path='') :
	file_type = None
	parent, file, ex_from = find_file_name(input_path)
	
	if output_path == '':
		output_path = parent + file + "." + ex_to
	else: 
		output_path += file + "." + ex_to
	
	print(output_path)

	for KEY in TYPE:
		for ext in TYPE[KEY]:
			if ext == ex_from:
				print('You are trying to convert a '+ KEY)
				file_type = KEY
				break
		if file_type != None:
			break

	(
	ffmpeg
	.input(input_path)
	.output(output_path)
	.run()
	)

if __name__ == '__main__':
	convert('audios/Macroblank - VANDAL CLUB - 01 vandal 1.mp3', 'wav')
