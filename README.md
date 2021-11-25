# SnykVulndb
SnykVulndb is library that used to check CVE for specific library by given library category (pip,npm,maven,composer), library name, and library by extracting html response from snyk.io page without any API-Key or registration.

**Disclaimer**
*This library is not official library from snyk. Use it as is without any guarantee or warranty. Your use of information from this library is at your own risk*

## How to Use
### Installation
```bash
pip install SnykVulndb
```

### Usage
```python
from SnykVulndb.CveChecker import CveChecker
checker = CveChecker()
##example 
# checker.getCveList(category,package_name,package_version)
checker.getCveList('pip','tensorflow','2.4.0')
```
```json
[{'id': 'CVE-2021-41214', 'score': '7.8'}, {'id': 'CVE-2021-41209', 'score': '5.5'}, {'id': 'CVE-2021-41199', 'score': '5.5'}, {'id': 'CVE-2021-41198', 'score': '5.5'}, {'id': 'CVE-2021-41197', 'score': '5.5'}, {'id': 'CVE-2021-41196', 'score': '5.5'}, {'id': 'CVE-2021-41200', 'score': '5.5'}, {'id': 'CVE-2021-41223', 'score': '7.1'}, {'id': 'CVE-2021-41205', 'score': '7.1'}, {'id': 'CVE-2021-41224', 'score': '7.1'}, {'id': 'CVE-2021-41216', 'score': '5.5'}, {'id': 'CVE-2021-41211', 'score': '7.1'}, {'id': 'CVE-2021-41201', 'score': '7.8'}, {'id': 'CVE-2021-41210', 'score': '7.1'}, {'id': 'CVE-2021-41204', 'score': '5.5'}, {'id': 'CVE-2021-41219', 'score': '7.8'}, {'id': 'CVE-2021-41215', 'score': '5.5'}, {'id': 'CVE-2021-41212', 'score': '7.1'}, {'id': 'CVE-2021-41221', 'score': '7.8'}, {'id': 'CVE-2021-41203', 'score': '7.8'}, {'id': 'CVE-2021-41213', 'score': '5.5'}, {'id': 'CVE-2021-41207', 'score': '5.5'}, {'id': 'CVE-2021-41227', 'score': '6.6'}, {'id': 'CVE-2021-41208', 'score': '8.8'}, {'id': 'CVE-2021-41202', 'score': '5.5'}]

```
Currently, supported categories are: pip, composer, npm, and maven

## Contact
mail: aryya.widigdha@yahoo.com    

License    
----     

MIT License
