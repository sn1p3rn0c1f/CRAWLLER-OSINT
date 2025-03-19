import whois

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return {
            'domain': domain,
            'registrar': w.registrar,
            'creation_date': str(w.creation_date),
            'expiration_date': str(w.expiration_date),
            'emails': w.emails
        }
    except Exception as e:
        return {"error": str(e)}
