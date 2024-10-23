database_mahasiswa = []


print("Selamat Datang di Siakad Mahasiswa")

def insert_semester():
	print("\nMasukkan Nama Semester\n")
	nama = input("Marksman Nama : ")
	data = {}
	data['nama semester'] = nama
	data['mata kuliah'] = []
	data['nilai'] = []
	database_mahasiswa.append(data)

def show_semester():
	print("\nDaftar Semester")
	for index,i in enumerate(database_mahasiswa):
		print(f"{index + 1}. {i['nama semester']}")
		if (len(i['mata kuliah']) == 0):
			print("\tSemester ini tidak punya mata kuliah")
		else:
			for indexj, j in enumerate(i['mata kuliah']):
				print(f"\t {indexj + 1}. {j} = {i['nilai'][indexj]} ")
		print("\n")

def show_matkul():
	print("\tDaftar mata kuliah")
	for index, i in enumerate(database_mahasiswa):
		if (len(i['mata kuliah']) == 0):
			print("\tbelum memiliki mata kuliah")
		else:
			for indexj, j in enumerate(i['mata kuliah']):
				print(f"\t {indexj + 1}. {j}")
		print("\n")

def insert_matkul():
	pilih_semester = int(input("Semester mana yang ingin anda tambahkan matkul nya : "))
	nama_matkul = str(input("Masukkan nama mata kuliah : "))
	nilai_matkul = int(input("Masukkan nilai matakuliah : "))

	database_mahasiswa[pilih_semester-1]['mata kuliah'].append(nama_matkul)
	database_mahasiswa[pilih_semester-1]["nilai"].append(nilai_matkul)

def remove_semester(pilihan_semester):
	if(pilihan_semester > len(database_mahasiswa)):
		return False
	else:
		if(pilihan_semester != 0):
			database_mahasiswa.pop(pilihan_semester - 1)
		return True

def remove_matkul(pilihan_semester, pilihan_matkul):
	if(pilihan_semester > len(database_mahasiswa)):
		return False
	else:
		if(pilihan_semester != 0):
			database_mahasiswa[pilihan_semester - 1]['mata kuliah'].pop(pilihan_matkul - 1)
			database_mahasiswa[pilihan_semester - 1]['nilai'].pop(pilihan_matkul - 1)
		return True

def rata_rata(pilihan_semester):
	for barang in database_mahasiswa:
		if barang == database_mahasiswa[pilihan_semester - 1]:
			total = 0
			for i in barang['nilai']:
				total = total + i
			hasil = total / len(barang['nilai'])
			print(f"Rata-rata nilai dari {database_mahasiswa[pilihan_semester - 1]['nama semester']} adalah : {hasil}")



def hasil_keseluruhan():
	print("\nTerimakasih telah menggunakan aplikasi ini")
	print("ini adalah hasil akhir")
	for index, i in enumerate(database_mahasiswa):
		print(f"{index + 1}.{i['nama semester']}")
		print(f"\tJumlah mata kuliah : {len(i['mata kuliah'])}")
		print("\n")

menu = 8

while(menu != 1):
	print("\n================================")
	print("1. keluar aplikasi")
	print("2. lihat semester")
	print("3. masukkan semester")
	print("4. hapus semester")
	print("5. masukkan mata kuliah")
	print("6. hapus mata kuliah")
	print("7. menghitung rata-rata nilai")
	print("\n================================")
	menu = int(input("masukkan menu anda: "))

	if(menu == 1):
		hasil_keseluruhan()
	elif(menu == 2):
		show_semester()
	elif(menu == 3):
		show_semester()
		insert_semester()
	elif(menu == 4):
		show_semester()
		is_it_success = False
		while(not is_it_success):
			removed_semester = int(input("Pilih Semester yang akan dihapus : "))
			is_it_success = remove_semester(removed_semester)
	elif(menu == 5):
		show_semester()
		insert_matkul()
	elif(menu == 6):
		show_matkul()
		yato = False
		while not yato:
			yayayato = int(input("Pilih semester yang kau mau pilih : "))
			yayato = int(input("Pilih matkul yang akan dihapus : "))
			yato = remove_matkul(yayayato, yayato)
	elif menu == 7:
		show_semester()
		semester = int(input("Pilih semester yang ingin di hitung rata-ratanya : "))
		rata_rata(semester)