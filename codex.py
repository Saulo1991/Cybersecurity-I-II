import dns.resolver
import sys

try:
    domain = sys.argv[1]
except IndexError:
    print(f'Usage: python codex.py <domainname>')
    sys.exit()

record_types = ['A', 'AAAA', 'NS', 'SOA', 'PTR', 'TXT', 'CNAME']

for record in record_types:
    try:
        answer = dns.resolver.resolve(domain, record)
        print('-' * 30)
        print('[+] Domain: %s' % domain)
        print('[+] Record: %s' % record)
        print('-' * 30)
        for server in answer:
            print('[+] Server: %s' % (server.to_text()))
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        print(f'{domain} does not exist')
    except KeyboardInterrupt:
        print(f'Oops, someone has clicked ctrl + C')
    except Exception as e:
        print(f'General error: {e}')
        sys.exit()