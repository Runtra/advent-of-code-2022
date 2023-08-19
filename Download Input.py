from datetime import date
import requests
import os
import cookiesKey

def main():

    cookies = cookiesKey.key

    baseDir = os.getcwd()
    year = os.path.basename(baseDir) # Agarra el nombre de la carpeta en la que esta este archivo, el cual es el año de la AOC

    url = "https://adventofcode.com/YEAR/day/DAY/input"
    url = url.replace("YEAR", year)
    

    today = date.today()

    maxDay = 25
    
    if today.year == int(year):
        if today.month == 12:
            if today.day < 25:
                maxDay = today.day

    
    for day in range(1,maxDay+1):
        pathExists = lambda path : os.path.exists(path)
        tempUrl = url.replace("DAY", str(day))

        if pathExists(f"./Day {day}/"):
            print(f"Day {day} exists")

            if not pathExists(f"./Day {day}/input.txt"): # Si el archivo no existe lo descarga y lo crea
                # Download input
                request = requests.get(tempUrl, cookies=cookies, allow_redirects=True)
                open(f"./Day {day}/input.txt", "wb").write(request.content)

        else:
            print(f"Day {day} doesn't exist")
            os.mkdir(f"./Day {day}")

            request = requests.get(tempUrl, allow_redirects=True, cookies=cookies)
            open(f"./Day {day}/input.txt", "wb").write(request.content)


if __name__ == "__main__":
    main()