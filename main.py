import json, pathlib

def check_key(key):
    return key.lower() == "email" or key.lower() == "token"

def redact(filepath):
    with pathlib.Path.open(filepath, "r", encoding="UTF-8") as file:
        f = json.load(file)

    update_count = 0

    if len(list(f.keys())) == 0: raise KeyError("ERROR: Object is empty")
    for key in f.keys():
        checking = key
        if not key in ['event','email', 'token', 'meta', 'items', 'message']:
            raise KeyError(f"Incorrect JSON")
        
        if check_key(key):
            f[key] = '[HIDDEN]'
            update_count += 1

    for key in f["meta"].keys():
        if check_key(key):
            f["meta"][key] = '[HIDDEN]'
            update_count += 1

    for index, item in enumerate(f["items"]):
        for key in item.keys():
            if check_key(key):
                f["items"][index][key] = '[HIDDEN]'
                update_count += 1
    
    return (f, update_count)


if __name__ == "__main__":
    res = redact("input.json")

    if res:
        print(f"Итоговый файл: {res[0]}\nКоличество изменений: {res[1]}")
        while True:
            choice = str(input("Сохранить изменения? (Y/N): "))
            if not choice in ['Y','N']:
                continue
            else:
                break
        if choice == "Y":
            with pathlib.Path.open("output.json", "w") as file:
                file.write(json.dumps(res[0], indent=4))