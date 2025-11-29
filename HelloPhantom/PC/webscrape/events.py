import csv

class EventScrape:
    def scrapeEventsWithDiagnostics():
        output = ""

        with open('C:/Users/johnharrison/Desktop/Hello Phantom/webscrape/data/events.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                print(lines)
                output += lines[1] + " on " + lines[0] + " at time " + lines[2] + ", "

            print(output)
            return output

    if __name__ == "__main__":
        scrapeEventsWithDiagnostics()