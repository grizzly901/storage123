print('Введите URL\'ы с новой строки (Нажмите дважды ENTER для завершения): \n')
a = []

while True:
    s = input()
    if not s:
        break
    a.append(s)

print("""
function openMultipleTabs(urlsArray) {
  urlsArray.forEach((url, key) => {
    if (key === 0) {
      window.open(url, `_blank_first_${key.toString()}`);
    } else {
      setTimeout(function () {
        window.open(url, `_blank_${key.toString()}`);
      }, 1500 * key);
    }
  });
}
""")

print(f"openMultipleTabs([")
for i in range(len(a)):
    if i != len(a) - 1:
        print(f"'{a[i]}',")
        continue
    print(f"'{a[i]}'")
print(']);')
