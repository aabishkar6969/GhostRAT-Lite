@echo off
echo ========== SYSTEM INFO ========== >> C:\PerfLogs\recon.txt
systeminfo >> C:\PerfLogs\recon.txt
echo ========== NETWORK INFO ========== >> C:\PerfLogs\recon.txt
ipconfig /all >> C:\PerfLogs\recon.txt
echo ========== USERS ========== >> C:\PerfLogs\recon.txt
net user >> C:\PerfLogs\recon.txt
echo ========== ADMINS ========== >> C:\PerfLogs\recon.txt
net localgroup administrators >> C:\PerfLogs\recon.txt
echo ========== RUNNING TASKS ========== >> C:\PerfLogs\recon.txt
tasklist /v >> C:\PerfLogs\recon.txt
echo ========== NETWORK CONNECTIONS ========== >> C:\PerfLogs\recon.txt
netstat -ano >> C:\PerfLogs\recon.txt
echo ========== DONE ========== >> C:\PerfLogs\recon.txt
