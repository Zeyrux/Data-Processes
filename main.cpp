#include <windows.h>
#include <tlhelp32.h>
#include <iostream>	
#include <string>
#include <fstream>
#include <ctime>

using namespace std;

int main( )
{
    time_t cur_time = time(nullptr);
    char *date = ctime(&cur_time);
    HANDLE hSnapShot=CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS,0);
    PROCESSENTRY32* processInfo=new PROCESSENTRY32;
    processInfo->dwSize=sizeof(PROCESSENTRY32);

    ofstream file;
    file.open("test.txt");

    file << "#NEW_CALL#" << endl;
    file << date;

    int index=0;
    while(Process32Next(hSnapShot,processInfo)!=FALSE)
    {
        file << "#NEW_PROCESS#: " << index << endl;
        file << "Module ID: " << processInfo->th32ModuleID << endl;
        file << "Parent Process ID: " << processInfo->th32ParentProcessID << endl;
        file << "Process ID: " << processInfo->th32ProcessID << endl;
        file << "Name: " << processInfo->szExeFile << endl;
        file << "Current Threads: " << processInfo->cntThreads << endl;
        file << "Current Usage: " << processInfo->cntUsage << endl;
        file << "Flags: " << processInfo->dwFlags << endl;
        file << "Size: " << processInfo->dwSize << endl;
        file << "Primary Class Base: " << processInfo->pcPriClassBase << endl;
        file << "Default Heap ID: " << processInfo->th32DefaultHeapID << endl;
    }
    CloseHandle(hSnapShot);
}

// https://www.codeproject.com/Articles/2851/Enumerating-processes-A-practical-approach