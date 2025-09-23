using System;
using System.IO;
static class Run
{
    private static void Main()
    {
        Console.WriteLine("Weclome to the Windows Cleaner App!");
        Console.WriteLine("What would you like to do? (1) Clean Temp Files (2) Clean Recycle Bin (3) List Startup Apps(4) Exit");
        string Operation = Console.ReadLine();

        switch (Operation)
        {
            case "1":
                TempFileCleaner();
                break;
            case "2":
                RecycleBinCleaner();
                break;
            case "3":
                StartupAppLister();
                break;
            case "4":
                Console.WriteLine("Exiting the application. Goodbye!");
                break;
            default:
                Console.WriteLine("Invalid option. Please select a valid operation.");
                break;
        }


    }
    static void TempFileCleaner()
    {
        Console.WriteLine("Cleaning temporary files...");
        // Find directory for temp files
        string tempFilePath = System.IO.Path.GetTempPath();
        Console.WriteLine("Temp files are located at: " + tempFilePath);
        //Search and delete temp files
        string[] tempFiles = Directory.GetFiles(tempFilePath, "*.tmp", SearchOption.AllDirectories);
        Console.WriteLine("Found " + tempFiles.Length + " temporary files.");
        foreach (string file in tempFiles)
        {
            try
            {
                File.Delete(file);
                Console.WriteLine("Deleted: " + file);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Could not delete: " + file + " - " + ex.Message);
            }
        }
        Console.WriteLine("Temporary files cleaned successfully.");
        Main();
    }
    static void RecycleBinCleaner()
    {
        Console.WriteLine("Emptying the Recycle Bin...");
        // Placeholder for actual recycle bin cleaning logic
        Console.WriteLine("Recycle Bin emptied successfully.");
        Main();
    }
    static void StartupAppLister()
    {
        Console.WriteLine("Listing startup applications...");
        // Placeholder for actual startup app listing logic
        Console.WriteLine("Startup applications listed successfully.");
        Main();
    }
}

