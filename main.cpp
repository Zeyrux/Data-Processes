#include <windows.h>
#include <tlhelp32.h>
#include <iostream>	
#include <string>
#include <fstream>

using namespace std;

int main( )
{
    cout<<endl<<"Running Processes"<<endl;
    HANDLE WINAPI CreateToolhelp32Snapshot(
        DWORD dwFlags,
        DWORD th32ProcessID
    );
    HANDLE hSnapShot=CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS,0);
    BOOL WINAPI Process32Next(
        HANDLE hSnapshot,
        LPPROCESSENTRY32 lppe
    );
    PROCESSENTRY32* processInfo=new PROCESSENTRY32;
    processInfo->dwSize=sizeof(PROCESSENTRY32);

    fstream file;
    file.open("test.txt");

    int index=0;
    int i=0;
    while(Process32Next(hSnapShot,processInfo)!=FALSE)
    {
        file<<endl<<"***********************************************";	
        file<<endl<<"\t\t\t"<<++index;
        file<<endl<<"***********************************************";	
        file<<endl<<"Parent Process ID: "<<processInfo->th32ParentProcessID;
        file<<endl<<"Process ID: "<<processInfo->th32ProcessID;
        file<<endl<<"Name: "<<processInfo->szExeFile;
        file<<endl<<"Current Threads: "<<processInfo->cntThreads;
        file<<endl<<"Current Usage: "<<processInfo->cntUsage;
        file<<endl<<"Flags: "<<processInfo->dwFlags;
        file<<endl<<"Size: "<<processInfo->dwSize;
        file<<endl<<"Primary Class Base: "<<processInfo->pcPriClassBase;
        file<<endl<<"Default Heap ID: "<<processInfo->th32DefaultHeapID;
        file<<endl<<"Module ID: "<<processInfo->th32ModuleID;
    }
    CloseHandle(hSnapShot);
}

// https://www.codeproject.com/Articles/2851/Enumerating-processes-A-practical-approach