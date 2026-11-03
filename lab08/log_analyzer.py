# Lab 8: Log File Analyzer
# Read and process application log entries

total = 0

print("ERROR REPORT")
print("----------------------------")

# Open and read the log file
with open("application.log", "r") as file:
    for line in file:
        # Extract timestamp using slicing
        timestamp = line [:19]

        # Find the seperator
        separator_index = line.find("|")

        # Standardize severity labels
        line = line.replace("error", "ERROR")
        line = line.replace("warning", "WARNING")

        # Split entry into fields
        fields = line.split("|")

        severity = fields[1].strip()
        message = fields[2].strip()

        # Include only errors and warnings
        if severity in ["ERROR", "WARNING"]:
            report = " - ".join(
                  [timestamp, severity, message]
            )
            print(report)
            total +=1

# Display summary
print()
print("total errors and warnings:", total)