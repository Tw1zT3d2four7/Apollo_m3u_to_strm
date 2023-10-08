$Title = "ApolloGroup"

$host.UI.RawUI.WindowTitle = $Title

Set-Location C:\Apollo_m3u_2_strm\scripts
timeout /t 240
python .\autoCRON.py
