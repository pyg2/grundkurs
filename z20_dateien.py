"""
FileReader fr = new FileReader(new File("text.txt"));
BufferedReader br = new BufferedReader br(fr);

String zeile = "";
StringBuilder sb = new StringBuilder();

while ((zeile = br.readLine()) != null) {
    sb.append(zeile);
}

System.out.println(sb);
fr.close();

String text = "";
FileReader fr = null;

try {
} catch (Exception e) {
} finally {
    fr.close()
}


"""

# with open('text.txt', encoding='UTF-8') as f:
#     text = f.readlines()
#
# print(text)
#
# f1 = None
#
# try:
#     f1 = open('text.txt')
#     f1.readlines()
# except:
#     print('Fehler')
# finally:
#     if f1:
#         f1.close()

with open('test2.txt', mode='a') as f2:
    f2.writelines(['hallo\n', 'welt'])
