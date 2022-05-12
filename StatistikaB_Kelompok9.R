# menentukan lembar kerja direktori ke dalam penyimpanan D, 
# direktori kuliah, subdirektori statistika, 
# dan subdirektori Data_tinggibadan
setwd("D:/KULIAH/STATISTIKA/Data_tinggibadan")

# menginstal packages
install.packages("readxl")

# menampilkan library Data_tingibadanmhs.xlsx
library(readxl)
Data_tingibadanmhs <- read_excel("Data_tingibadanmhs.xlsx")
View(Data_tingibadanmhs)

# mendefinisikan kembali Data_tingibadanmhs ke variabel tabel 
tabel <- Data_tingibadanmhs

# mengambil data frame dan membuat kolomnya dapat diakses
attach(tabel)

# menentukan total frekuensi
totalf = sum(`Frekuensi (f)`)

# mengubah type data menjadi numeric
fx <- as.numeric(f.Xi)

# menentukan mean data kelompok
mean = sum(fx)/rataf

# mendeklarasikan diket median dengan data frame
KetMedian <- data.frame (
  keterangan = c("b", "n", "F", "f", "p"),
  nilai = c(160.5, 100, 43, 38, 10)
)

# mendefinisikan keterangan supaya dapat dioperasikan
KetMedian
b = 160.5
n = 100
F = 43
f = 38
p = 10

# menentukan median data kelompok
median1= b + p * ((1/2*n-F)/f)

# mendeklarasikan diket median dengan data frame
KetModus <- data.frame (
  keterangan = c("b", "p", "b1", "b2"),
  nilai = c(160.5, 10, 2, 10)
)

# mendefinisikan keterangan supaya dapat dioperasikan
KetModus
b = 160.5
n = 10
b1 = 38-36
b2 = 38-18

# menentukan modus data kelompok
modus1= b + p * (b1/(b1+b2))

# menampilkan isi tabel
tabel 

# menentukan minimal dan maksimal dari tabel pada kolom titik tengah
max <- max(tabel$`titik tengah (Xi)`)
min <- min(tabel$`titik tengah (Xi)`)

# menentukan simpangan dengan mengurangi nilai max dengan nilai min
range1 = max - min

# menentukan total simpangan mutlak
totalsimpangan =  sum(tabel$`f.|Xi - X|`)

# menentukan mean deviasi
MeanDeviasi = (sum(tabel$`f.|Xi - X|`))/(sum(tabel$`Frekuensi (f)`))

# menentukan total simpangan baku
totalsimbaku = (sum(tabel$`f.(Xi - X)^2`))/(sum(tabel$`Frekuensi (f)`))

# menentukan standart deviasi
StandarDeviasi = sqrt(totalsimbaku)


