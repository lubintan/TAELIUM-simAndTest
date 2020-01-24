#!/usr/bin/expect -f

spawn bash -c "scp -r -i Jarvis-2.pem /Users/Lubin/skynet/preIco/* ubuntu@ec2-13-127-21-116.ap-south-1.compute.amazonaws.com:~/Desktop/preIco/"
expect {
			-re ".*sword.*" {
				exp_send "Jarvis-2\r"
			}
}

interact