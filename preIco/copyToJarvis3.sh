#!/usr/bin/expect -f

spawn bash -c "scp -r -i Jarvis-3.pem /Users/Lubin/skynet/preIco/* ubuntu@ec2-13-231-179-130.ap-northeast-1.compute.amazonaws.com:~/Desktop/preIco"
expect {
			-re ".*sword.*" {
				exp_send "Jarvis-3\r"
			}
}

interact