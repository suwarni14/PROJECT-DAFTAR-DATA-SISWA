print ('''Halo Selamat Datang\n''')
daftar_data_siswa = [
    ['SW101','Ani','Wanita','10','Jakarta'],
    ['SW102','Fadil','Pria','12','BSD'], 
    ['SW103','Tasya','Wanita','13','Surabaya']]

def Menu1Sub1 ():
    if len(daftar_data_siswa) != 0:
        print ('Daftar Data Siswa\n')
        print ('NIS\t|Nama\t|Gender\t|Umur\t|Alamat')                   #i = baris, 0 = kolom
        for i in range (len(daftar_data_siswa)):
            print (f'{daftar_data_siswa[i][0]}\t|{daftar_data_siswa[i][1]}\t|{daftar_data_siswa[i][2]}\t|{daftar_data_siswa[i][3]}\t|{daftar_data_siswa[i][4]}')
        print ('')
    else :
        print('Data tidak tersedia')

def Menu1Sub2 ():
    inputMenu1Sub2 = input('Silahkan Masukan NIS Siswa : ').upper()
    print(f'Data Siswa {inputMenu1Sub2}')
    for i in range(len(daftar_data_siswa)):
        if inputMenu1Sub2 == daftar_data_siswa[i][0]:       #i = baris, 0 = kolom
            print ('NIS\t|Nama\t|Gender\t|Umur\t|Alamat')           
            print (f'{daftar_data_siswa[i][0]}\t|{daftar_data_siswa[i][1]}\t|{daftar_data_siswa[i][2]}\t|{daftar_data_siswa[i][3]}\t|{daftar_data_siswa[i][4]}')
            break
    else:
        print('NIS yg dimasukkan salah, silahkan masukkan yg benar')

def Menu2Sub1 ():
    nis = str(input ('NIS : ')).upper()
    nama = str(input('Nama Siswa : '))
    gender = str(input('Gender : '))
    umur = str(input('Umur: '))
    alamat = str(input('Alamat : '))

    daftar_data_siswa.append([nis, nama, gender,umur,alamat])
    
    print ('Daftar Data Siswa\n')
    print ('NIS\t|Nama\t|Gender\t|Umur\t|Alamat')
    for i in range (len(daftar_data_siswa)):
        print (f'{daftar_data_siswa[i][0]}\t|{daftar_data_siswa[i][1]}\t|{daftar_data_siswa[i][2]}\t|{daftar_data_siswa[i][3]}\t|{daftar_data_siswa[i][4]}')
        print ('')

def Menu3Sub1 ():
    inputMenu3Sub1 = input('Silahkan Masukan NIS Siswa : ').upper()
    print(f'Data Siswa {inputMenu3Sub1}')

    for i in range(len(daftar_data_siswa)):
        if inputMenu3Sub1 == daftar_data_siswa [i][0]:
            print ('NIS\t|Nama\t|Gender\t|Umur\t|Alamat')           
            print (f'{daftar_data_siswa[i][0]}\t|{daftar_data_siswa[i][1]}\t|{daftar_data_siswa[i][2]}\t|{daftar_data_siswa[i][3]}\t|{daftar_data_siswa[i][4]}')

            while True:
                inputYN = input('Apakah lanjut update atau tidak (Y/N): ').upper()
            
                if inputYN == 'Y':
                    inputKolom = input('Masukkan Nama Kolom yang ingin diubah: ').capitalize()
                    inputDataBaru = input('Masukkan Data Baru: ')
                    noKolom = 0
                    if inputKolom == 'NIS':
                        noKolom = 0
                    elif inputKolom == 'Nama':
                        noKolom = 1
                    elif inputKolom == 'Gender':
                        noKolom = 2
                    elif inputKolom == 'Umur':
                        noKolom = 3
                    elif inputKolom == 'Alamat':
                        noKolom = 4
                    else:
                        print('Yang Anda Masukkan Salah')
                    
                    while True:
                        inputYN2 = input('Apakah lanjut update atau tidak (Y/N): ').upper()          #konfirmasi kedua

                        if inputYN2 == 'Y':
                            daftar_data_siswa[i][noKolom] = inputDataBaru                            #proses update 
                            print('Data telah di-update')
                            break
                        
                        elif inputYN2 == 'N':
                            print('Data tidak jadi di-update')
                            break 
                        
                        else:
                            print('Masukkan Y/N saja')
                            continue
                    
                    break

                elif inputYN == 'N':
                    print('Data tidak jadi diubah')
            
                else:
                    print('Masukkan Y/N saja')
                    continue
            break
    else:
        print('NIS yg anda input salah, silahkan masukkan yang benar')


def Menu4Sub1 ():
    listNIS = []
    for i in daftar_data_siswa:
        listNIS.append(i[0])
    while True:
        nis = str (input('NIS Siswa yang Ingin Dihapus : ')).upper()
        if nis in listNIS:
            while True:
                tanya = input('Apakah anda yakin untuk menghapus data (y/n): ').upper()
                if tanya == 'Y':
                    ygdihapus = listNIS.index(nis)
                    del daftar_data_siswa[ygdihapus]
                    print(f'Data {nis} berhasil terhapus')
                    break
                elif tanya == 'N':
                    print(f'Data {nis} tidak jadi dihapus')
                    break                    
                else:
                    continue
        elif nis not in listNIS:
            print(f'Data {nis} tidak tersedia')
            break
        break

#################################################################################################################
       
while True :                        #Menu Utama
    menu = int (input('''Silahkan Pilih:
    1. Daftar Data Siswa
    2. Menambahkan Data Siswa
    3. Mengubah Data Siswa
    4. Menghapus Data Siswa
    5. Exit Program
Menu yang ingin dijalankan : '''))
    print('------------------------------------------------')
    print('------------------------------------------------')

#################################################################################################################
    if menu == 1 :          #Menampilkan Data Siswa    
        while True: 
            inputSubMenu = input ('''\nSilahkan pilih submenu:  
            1. Menampilkan Seluruh Data Siswa
            2. Menampilkan Data Siswa Tertentu 
            3. Kembali Ke Menu Utama
Menu yang ingin dijalankan : ''')

            if inputSubMenu == '1':
                Menu1Sub1()
                
            elif inputSubMenu == '2':
                Menu1Sub2()
            
            elif inputSubMenu == '3':
                break
            else :
                print('Silahkan Masukkan Angka yang Benar')

#########################################################################################################

    elif menu == 2 :      #Update Data Siswa
        while True: 
            inputSubMenu = input ('''Silahkan pilih submenu:  
            1. Menambahkan Data Siswa Baru
            2. Kembali Ke Menu Utama
Menu yang ingin dijalankan : ''')

            if inputSubMenu == '1':
                Menu2Sub1()
                
            elif inputSubMenu == '2':
                break
            
            else :
                print('Silahkan Masukkan Angka yang Benar')

#################################################################################################################

    elif menu == 3 :            #Mengubah Data Siswa
        while True: 
            inputSubMenu = input ('''Silahkan pilih submenu:  
            1. Mengubah Data Siswa 
            2. Kembali Ke Menu Utama
Menu yang ingin dijalankan : ''')

            if inputSubMenu == '1':
                Menu3Sub1()
                
            elif inputSubMenu == '2':
                break
            
            else :
                print('Silahkan Masukkan Angka yang Benar')

#################################################################################################################

    elif menu == 4 :            #Menghapus Data Siswa
        while True: 
            inputSubMenu = input('''Silahkan pilih submenu:  
            1. Menghapus Data Siswa 
            2. Kembali Ke Menu Utama
Menu yang ingin dijalankan : ''')

            if inputSubMenu == '1':
                Menu4Sub1()
                
            elif inputSubMenu == '2':
                break
            
            else :
                print('Silahkan Masukkan Angka yang Benar')
  
    else :
        print ('Keluar Program, Terima Kasih')
        break