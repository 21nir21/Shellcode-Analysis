import pylibemu

# Enter the Shellcode here
shellcode = ".....\x\x\x\x\x\x....."

emulator = pylibemu.Emulator()
offset = emulator.shellcode_getpc_test(shellcode)

if offset >= 0:
  print "[+] IS SHELLCODE!"
else:
  print "[-] NOT SHELLCODE!"

emulator.prepare(shellcode, offset)
emulator.test()
print emulator.emu_profile_output
