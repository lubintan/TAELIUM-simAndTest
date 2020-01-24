#!/usr/bin/expect -f

spawn bash -c "scp -r -i Jarvis-1.pem /Users/Lubin/skynet/preIco/* ubuntu@ec2-18-222-73-206.us-east-2.compute.amazonaws.com:~/Desktop/preIco"
expect {
			-re ".*sword.*" {
				exp_send "Jarvis-1\r"
			}
}

interact