*Windows Server 2022 AD Implementation*
**1. Windows server Eval free**
- search https://www.microsoft.com/en-us/evalcenter/download-windows-server-2022 and download the 64-bit edition  ISO.

**2. VirtualBox setup**
- Hit the new button to create a new machine
- Name the new machine AD Lab Server
- Under ISO Image select the Windows Server ISO from step one.
- Make sure the OS option is set to Microsoft Windows then select finish, do not check the unattended installation option.
- Open the settings on the machine and make the following changes.
  >1. Go to the system section and set "Base Memory" to 8000MB.
  >2. Then open the Processor tab and set "Number of CPUs to 2.
  >3. Next Navigate to the Network section and set the Attached to option to "Internal Network" and Name to AD_LAB then set Adapter 2 to NAT. 
- click ok and double click the new machine to start it.

  **Installation**
  - make sure all the information is correct before continuing and intalling
  - on the window that says Microsoft Server Operating System Setup choose the option that says Windows Server 2022 Standard Evaluation (Desktop Experience)
  - accept the license terms.
  -  choose custom install and click next.
  -  Create your password (ex:ADLab445%).
  -  Rename the server to DC01 then hit Restart Now and continue.
  -  
     **Configure static IP**
  > 1. click the network icon at the bottom right of the taskbar.
  > 2. click change adapter options.
  > 3. Right click Ethernet and click properties.
  > 4. Double click Internet Protocol Version 4(TCP.IPc4)
  > 5. Then click Use the following IP address.
  > >IP address: 192.168.10.10
  > >Subnet mask: 255.255.255.0
  > >Default gateway: (Blank)
  > >Preferred DNS: 192.168.10.10
  > >Hit Ok
  
  **Promote to Domain Controller**
  - Go back to the server manager
  - Hit Add Roles and Features
  - When the wizard opens hit next, make sure role-based or feature-based installation is clicked then hit next.
  - Highlight your server and hit next.
  - 
  - Server roles selection:
  - >Active Directory Domain Services
    >Hit add features
    >DNS Server
    >Hit add features
    >hit next
  - Features selection: (leave defaults)\
  - Click next on AD DS.
  - Click next on DNS Server.
  - On Confirmation check restart the destination server automatically if required then hit install.
  - once the installation is finished close the window
  - Next click the yello nw triangle at the top of the screen and click Promote this server to a domain controller.
  - Click add a new forest then set the root domain name to corp.local then click next.
  - Make sure Domain Name System (DNS) server and Global Catalog(GC) are  the only two options checked.\
  - Create your password (ex:ADLab445%).
  - Ignore the warning and click next.
  - Hit Next as long as the NetBIOS domain name is CORP
  - contiue clicking next until the prerequisites checks start.
  - Click install as long as the prerequisite checks have passed successfully, ignore warnings.
 **Forward requeste to the internet**
  -go to the server manager
  -go to tools>DNS then right click the server name.
  -hit properties then the forwarders tab


  **Client Installation** a new machine
  - Name the new machine AD Lab Client
  - Under ISO Image select the Wi
  - install the windows 11 ISO from microsoft.com
  - Hit the new button to create Windows 11 ISO from step one.
  - Make sure the OS option is set to Microsoft Windows then select finish, do not check the unattended installation option.
  - Open the new machines settings
  - Set Ram to 8000mb
  - Set CPU to 2 cores
  - Set Network Adapter 1 to Internal network
  - Set Network Adapter 2 to NAT
  - Open the client machine and start the windows setup.
  - hit next on language settings and next on keyboard settings.
  - click the Install Windows 11, check the agree button then hit next.
  - On the Product Key page and hit "I don't have a product key" option at the bottom of the page.
  - then choose  the Windows Pro 11 for workstations image.
  - Allow the image to finish.

  **Domain**
  
  - name the PC to CLIENT01
  - Set DNS to 192.168.10.10
  - hit setup for work or school
  - Under the email form click sign-in options
  - Then select domain sign in instead and set the name as CLIENT
  - Create your password (ex:ADLab445%).
  - Open control panel>Network and Internet>network and sharing center>change adapter settings.
  - right click ethernet and go to properties
  - double click Internet Protocol Version 4 (IPv4)
  - check Use the following DNS server:
>IP address: 192.168.10.20
>Subnet mask: 255.255.255.0
>Preferred DNS: 192.168.10.10
  - then go to settings>system>advanced system settings
  - click under the Computer Name tab
  - click change at the bottom and for Domain enter: corp.local
  - now enter the DC credentials.
  - Congragulatons you can now sign in the client device with the DC credentials because AD is controlled by the DC(Domain Controller)

    **Installing SIEM**
 - Install the Wazuh all in one OVA
 - go to virtual box and click import and import the OVA you just installed.
 - next set adapter one to internal network and make the name AD_LAB just like the others.
 - then adapter 2 on NAT.
 - Open the machine and login using the login info that the terminal gives you.
 - IP Config:
   >1. sudo ip addr add 192.168.10.50/24 dev eth1.
   >2. sudo ip link set eth1 up.
   
   > you must do this at every logon.
 **Starting the SIEM**
 -Open the client machine and type the https://192.168.10.50 into the web browser.
 - login using the username admin and the password admin.
 - go to deploy new agent
 - follow all of the steps
 - give the clien and the attacking machine a new network adapter on host only(VMs cannot communicate with each other over the internet so the host will act as the internet.)
 - 


  
  
