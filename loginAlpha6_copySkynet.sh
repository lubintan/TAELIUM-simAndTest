#!/usr/bin/expect -f

spawn bash -c "scp -r -i /Users/Lubin/skynet/* ubuntu@ec2-54-255-200-180.ap-southeast-1.compute.amazonaws.com:~/Desktop/skynet"
expect {
			-re ".*sword.*" {
				exp_send "Alpha-6\r"
			}
}

interact