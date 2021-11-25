import requests
import json
import time
import lxml.html as lh

class CveChecker:
    def __init__(self):
	    pass
    def getLandingPage(self,category,lib_name,lib_version):
        url = 'https://snyk.io/vuln/'+category+':'+lib_name+'@'+lib_version
        content = requests.get(url)
        if content.status_code >= 300:
            raise Exception("Library name seems incorrect / we can not found in snyk. Please check it manually here:"+url)
        return content
    def getVulnList(self,category,lib_name,lib_version):
        landing_page = self.getLandingPage(category,lib_name,lib_version)
        doc = lh.fromstring(landing_page.text)
        raw_vuln_list = doc.xpath('//table')[1].xpath('tbody/tr')
        vuln_list = []
        for vuln in raw_vuln_list:
            try:
                vuln_list.append(vuln.xpath('td')[0].xpath('span/a')[0].attrib['href'])
            except:
                pass
        return vuln_list
    def getCveList(self,category,lib_name,lib_version):
        if category not in ["npm","pip","composer","maven"]:
            return "You are scanning unsupported category. Please try something else"
        vuln_list = self.getVulnList(category,lib_name,lib_version)
        cves = []
        for vuln in vuln_list:
            cve = {}
            try:
                cve_page = requests.get('https://snyk.io'+vuln)
                doc = lh.fromstring(cve_page.text)
                cve['id'] = doc.xpath('//a[contains(@id, "CVE-20")]')[0].attrib['id']
                cve['score'] = doc.xpath('//div[contains(@id, "severity-widget-score")]')[0].attrib['data-snyk-test']
                cves.append(cve)
            except:
                pass
        return cves
