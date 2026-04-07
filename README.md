1. Pada saat inisialisasi tugas1 bernilai false dan tugas2 juga

2. kemudian di cek kondisi pada fungsi thread1_step() jika tugas1 bernilai true tugas1 diubah menjadi true dan status hold kemudian sebaliknya 

3. thread2_step juga sama untuk mekanisme fungsi dengan thread1_step()

4. kemudian dilakukan perulangan untuk menjalan fungsi thread1_step dan thread2_step sebanyak 10 kali dengan selisih waktu 0.5s 
5. setelah itu di cek kondisi per iterasi

6. pada saat iterasi pertama kedua fungsi menampilkan return hold nah pada iterasi kedua karena kedua variable bernilai true maka masuk pada kondisi elif dan return wait sehingga kedua tugas saling menunggu satu sama lain dan mengjasilkan deadlock 
