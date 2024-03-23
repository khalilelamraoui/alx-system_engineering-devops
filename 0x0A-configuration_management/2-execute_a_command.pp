# 2-execute_a_command
# manifest that kills the process killmenow


exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
  provider => 'shell',
}
