<section class="main-contents-container"><div class="MuiContainer-root MuiContainer-maxWidthLg MuiContainer-fixed css-6cznyo"><div class="MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-2 css-isbt42"><div class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-10 MuiGrid-grid-sm-10 MuiGrid-grid-md-8 MuiGrid-grid-lg-8 css-1tryykw"><div class="markdown-container js-toc-content" style="overflow-wrap: break-word;"><h2 class="MuiTypography-root MuiTypography-h2 css-1d8u6kn" id="overview" level="2" index="0" siblingcount="55" node="[object Object]">Overview</h2>
<p index="1" siblingcount="55">Designing a system or application for security involves incorporating security considerations into the design process from the very beginning, in order to prevent vulnerabilities from arising in the first place. Thus, <em>designing for security</em> refers to the practice of incorporating security considerations into the design and development of a system, product, or service, and can include the use of secure coding practices, threat modeling, and security testing to identify and mitigate potential vulnerabilities.</p>
<p index="2" siblingcount="55">In this blog, I explore how designing for security makes a system more resilient to attack and protects the confidentiality, integrity, and availability of the data and resources that it processes. I address why an important aspect of overall security strategy is to implement these measures throughout the entire development life cycle.</p>
<h2 class="MuiTypography-root MuiTypography-h2 css-1d8u6kn" id="how-to-design-for-security" level="2" index="3" siblingcount="55" node="[object Object]">How to Design for Security</h2>
<p index="4" siblingcount="55">Designing for security involves incorporating security considerations into the design of systems and software from the beginning of the development process. This approach can help to prevent vulnerabilities from arising in the first place, making it more difficult for attackers to exploit them.</p>
<p index="5" siblingcount="55">Here are measures to take in designing for security:</p>
<ul>
<li><em>Use a threat modeling methodology.</em> Identify the potential threats to a system or application and design the system to mitigate or eliminate those threats. Use a threat modeling methodology such as STRIDE to identify and evaluate potential security threats.</li>
<li><em>Use secure design patterns.</em> Use design patterns that have been proven to be secure, such as the principle of least privilege, to ensure that systems and software are designed with security in mind.</li>
<li><em>Use secure communication protocols.</em> Use secure communication protocols such as HTTPS to protect the integrity of data transmitted over the network.</li>
<li>*Use encryption: Use encryption to protect sensitive data, both at rest and in transit, to protect it from unauthorized access and disclosure.</li>
<li><em>Use secure development methodologies.</em> Use secure development methodologies such as OWASP (Open Web Application Security Project) to ensure that secure coding practices are followed throughout the development process.</li>
<li><em>Incorporate security testing.</em> Incorporate security testing into the development process to identify and address vulnerabilities early on.</li>
<li><em>Use secure configuration.</em> Ensure that systems and software are configured securely to prevent unauthorized access and elevation of privilege.</li>
<li><em>Conduct regular security assessments.</em> Regularly assess the security of your systems and networks to identify and address potential vulnerabilities.</li>
</ul>
<h2 class="MuiTypography-root MuiTypography-h2 css-1d8u6kn" id="stride-threat-modeling" level="2" index="7" siblingcount="55" node="[object Object]">STRIDE Threat Modeling</h2>
<p index="8" siblingcount="55">The <a class="MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways css-ir33j0" target="_blank" href="https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats#stride-model">STRIDE</a> methodology for threat modeling provides a sound approach for preventing most security issues. Each letter of the STRIDE nomenclature - which stands for Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, and Elevation of privilege - represents a specific type of security threat that can be mitigated through appropriate security controls.</p>
<p index="9" siblingcount="55"><img src="/img/STRIDE_ThreatModel.png" alt="STRIDE"></p>
<p index="10" siblingcount="55">Let's explore how each component of this modeling methodology contributes to identifying and evaluating potential security threats to a system or application.</p>
<h3 class="MuiTypography-root MuiTypography-h3 css-1hl2c6a" id="spoofing" level="3" index="11" siblingcount="55" node="[object Object]">Spoofing</h3>
<p index="12" siblingcount="55">Spoofing refers to the act of pretending to be someone else in order to gain unauthorized access to information or resources.</p>
<p index="13" siblingcount="55">For example, an attacker may use spoofed email addresses or phone numbers to impersonate a legitimate user and gain access to sensitive information. Another
example of API spoofing would be an attacker who creates a fake API that mimics a legitimate API, and then tricks users into interacting with the fake API. The attacker could then use the fake API to steal sensitive information or perform unauthorized actions.</p>
<p index="14" siblingcount="55">To prevent spoofing, we can implement these security measures:</p>
<ul>
<li><em>Implement user authentication.</em> Use secure authentication methods such as two-factor authentication to ensure that only authorized users can access resources. Use secure authentication methods such as OAuth and JWT to ensure that only authorized users can access the API. Use role-based access controls to ensure that users have the minimum level of access necessary to perform their job.</li>
<li><em>Validate input.</em> Validate all input data to ensure that it is coming from a trusted source and that it is in the correct format, to prevent attackers from injecting malicious data.</li>
<li><em>Use encryption.</em> Use Secure Sockets Layer (SSL) or Transport Layer Security (TLS)
encryption to protect sensitive data, both at rest and in transit, to protect it from unauthorized access and disclosure.</li>
<li><em>Use anti-spoofing technologies.</em> Implement anti-spoofing technologies such as Sender Policy Framework (SPF) and Domain-based Message Authentication, Reporting &amp; Conformance (DMARC) to verify the authenticity of incoming emails and prevent email spoofing.</li>
<li><em>Use network security.</em> Implement network security measures such as firewalls, intrusion detection and prevention systems to prevent unauthorized access to resources.</li>
<li><em>Use secure communication protocols.</em> Use secure communication protocols such as HTTPS to protect the integrity of data transmitted over the network.</li>
<li><em>Use API Gateway.</em> Use API Gateway to provide a single-entry point for API access and to perform security-related tasks such as authentication, access control, and rate limiting.</li>
<li><em>Use API Management.</em> Use API management platform to create and manage API policies, to ensure.</li>
<li><em>Use a web application firewall (WAF) to detect and prevent malicious requests.</em></li>
<li><em>Use a CAPTCHA system to block automated bots and scripts which can be used to spoof.</em></li>
</ul>
<h3 class="MuiTypography-root MuiTypography-h3 css-1hl2c6a" id="tampering" level="3" index="16" siblingcount="55" node="[object Object]">Tampering</h3>
<p index="17" siblingcount="55">Tampering refers to an attacker modifying the communication between an application and an API in order to perform unauthorized actions or gain access to sensitive data. Tampering can have serious consequences that include data loss, system downtime, and loss of trust in the system.</p>
<p index="18" siblingcount="55">An example of tampering would be for an attacker to intercept a communication between an application and an API, and alter the request to gain unauthorized access to sensitive data or perform unauthorized actions; in such a case, the attacker might intercept a request to retrieve a user's account balance and alter the request to transfer money from the account. Another example of tampering would be for the attacker to intercept a network communication and alter the data being transmitted; the purpose of this action would be to disrupt the communication or change the meaning of the data being transmitted.</p>
<p index="19" siblingcount="55">To prevent tampering, we can implement these security measures:</p>
<ul>
<li><em>Use digital signatures and non-repudiation techniques.</em> Use digital signatures and other non-repudiation techniques such as time-stamping to prove the authenticity and integrity of a transaction.</li>
<li><em>Use secure communication protocols.</em> Use secure communication protocols such as HTTPS to protect the integrity of data transmitted over the network.</li>
<li><em>Use tamper-proofing techniques.</em> Implement tamper-proofing techniques such as code signing and digital certificates to protect software and firmware from unauthorized modification.</li>
<li><em>Use version control.</em> Use version control systems to track changes to software and configuration files, and to ensure that only authorized changes are made.</li>
<li><em>Regularly backup data.</em> Regularly backup critical data and store it in a secure location, to restore data in the event of tampering.</li>
<li><em>Use of checksums and hashes to validate the integrity of the data.</em></li>
<li><em>Using message authentication codes (MACs) or digital signatures to ensure the integrity of the data being transmitted.</em> This would allow the receiver to verify that the data has not been tampered with during transit.</li>
<li><em>Using access control mechanisms such as role-based access control (RBAC) or attribute-based access control (ABAC) to restrict access to sensitive data.</em></li>
</ul>
<h3 class="MuiTypography-root MuiTypography-h3 css-1hl2c6a" id="repudiation" level="3" index="21" siblingcount="55" node="[object Object]">Repudiation</h3>
<p index="22" siblingcount="55">Repudiation refers to the ability of a user or attacker to deny having performed a specific action or transaction. This can have serious consequences, including financial losses, legal disputes, and damage to an organization's reputation.</p>
<p index="23" siblingcount="55">An example of repudiation would be for an attacker to successfully gain access to a user's account in an online banking system and make unauthorized transactions; the attacker could then deny having made the transactions, and the victim would be held liable for the unauthorized actions. Another example of repudiation would be an employee denying having sent a confidential email, even though the forged email can be traced back to their account.</p>
<p index="24" siblingcount="55">To prevent repudiation, we can implement these security measures:</p>
<ul>
<li><em>Logging and Auditing.</em> Maintain a detailed log of all actions taken within the system. This will help to trace back any suspicious activity and to identify the user who performed the action. Implement automated auditing to regularly review the logs for any suspicious activity. Additionally, it's important to keep the logs and audit trails in a secure location and have a retention policy to keep them for a certain period of time, to be able to use them as evidence if needed.</li>
<li><em>Use an intrusion detection system (IDS) to detect and alert on any unauthorized access or tampering attempts.</em></li>
<li><em>Use multifactor authentication.</em> Use multifactor authentication methods to increase the difficulty of impersonating a user and to make it harder for a user to deny performing an action.</li>
<li><em>Use tamper-proofing techniques.</em> Implement tamper-proofing techniques such as code signing and digital certificates to protect software and firmware from unauthorized modification.</li>
<li><em>Implement authentication and access controls.</em> Use secure authentication methods such as two-factor authentication to ensure that only authorized users can access resources, and limit access to sensitive data and resources to only those who need it.</li>
<li><em>Use digital signatures and non-repudiation techniques.</em> Use digital signatures and other non-repudiation techniques such as time-stamping to prove the authenticity and integrity of a transaction.</li>
</ul>
<h3 class="MuiTypography-root MuiTypography-h3 css-1hl2c6a" id="information-disclosure" level="3" index="26" siblingcount="55" node="[object Object]">Information disclosure</h3>
<p index="27" siblingcount="55">Information disclosure involves the exposure of information to individuals who are not supposed to have access to it. This can include sensitive information such as login credentials, personal information, or confidential business information.</p>
<p index="28" siblingcount="55">An example of information disclosure would be for an attacker to gain access to a database containing sensitive information such as customer data or financial records; the attacker could then exfiltrate or publish this data. Another example of information disclosure would be for an attacker to intercept network communication and read the data being transmitted.</p>
<p index="29" siblingcount="55">To prevent information disclosure, we can implement these security measures:</p>
<ul>
<li><em>Use data loss prevention (DLP) solutions.</em> Use DLP solutions to prevent sensitive data from being exfiltrated or leaked.</li>
<li><em>Implement access controls.</em> Limit access to sensitive data and resources to only those who need it and use role-based access controls to ensure that users have the minimum level of access necessary to perform their job.</li>
<li><em>Use network security.</em> Implement network security measures such as firewalls, intrusion detection and prevention systems to prevent unauthorized access to resources.</li>
<li><em>Use encryption.</em> Encrypt sensitive data, both at rest and in transit, to protect it from unauthorized access and disclosure.</li>
<li><em>Use secure coding practices.</em> Implement secure coding practices and conduct code reviews to identify and remediate potential vulnerabilities.</li>
</ul>
<h3 class="MuiTypography-root MuiTypography-h3 css-1hl2c6a" id="denial-of-service" level="3" index="31" siblingcount="55" node="[object Object]">Denial of Service</h3>
<p index="32" siblingcount="55">Denial of service (DoS) attacks aim to make a system or network unavailable to its intended users by overwhelming it with a large amount of traffic or requests.</p>
<p index="33" siblingcount="55">An example of a DoS attack would be a distributed denial of service (DDoS) attack, where the attacker uses a network of compromised devices to flood a target server or network with a large amount of traffic, making it unavailable to legitimate users. Another example of a DoS attack would be a resource depletion attack, where the attacker floods a targeted server with many requests, overwhelming its resources and making it unavailable.</p>
<p index="34" siblingcount="55">To prevent denial of service, we can implement these security measures:</p>
<ul>
<li><em>Use network security devices.</em> Implement network security devices such as firewalls and intrusion prevention systems to filter and block malicious traffic.</li>
<li><em>Use DDoS mitigation services.</em> Use DDoS mitigation services to protect against DDoS attacks.</li>
<li><em>Implement rate limiting.</em> Implement rate limiting to prevent resource depletion attacks by limiting the number of requests a user or IP address can make to the system.</li>
<li><em>Use Content Delivery Network (CDN).</em> Use Content Delivery Network (CDN) to distribute the traffic over many servers, making it difficult for an attacker to target a specific server.</li>
<li><em>Have an incident response plan.</em> Have an incident response plan in place to quickly respond to a DoS attack and minimize the impact.</li>
</ul>
<h3 class="MuiTypography-root MuiTypography-h3 css-1hl2c6a" id="elevation-of-privilege--enable-least-privilege" level="3" index="36" siblingcount="55" node="[object Object]">Elevation of privilege / Enable least privilege</h3>
<p index="37" siblingcount="55">When an attacker gains access to a higher level of permissions than they are supposed to have, it can allow them to perform actions that would normally be restricted, such as modifying or deleting sensitive data or gaining access to restricted resources.</p>
<p index="38" siblingcount="55">An example of an elevation of privilege attack would be for an attacker to exploit a vulnerability in a web application or an API to gain access to the underlying operating system and execute arbitrary code with elevated privileges. Another example of an elevation of privilege attack would be for an attacker to gain access to an administrator's account, then use that account to gain access to restricted resources or perform actions that would normally be restricted.</p>
<p index="39" siblingcount="55">To prevent elevation of privilege attacks, we can implement these security measures:</p>
<ul>
<li><em>Implement Least Privilege.</em> Limit access to sensitive data and resources to only those who need it and use role-based access controls to ensure that users have the minimum level of access necessary to perform their job.</li>
<li><em>Use input validation.</em> Validate all input data to ensure that it is coming from a trusted source and that it is in the correct format, to prevent attackers from injecting malicious data.</li>
<li><em>Use anti-malware and endpoint protection.</em> Use anti-malware and endpoint protection to protect against malware and other malicious software.</li>
<li><em>Use Secure Coding practices.</em> Implement secure coding practices and conduct code reviews to identify and remediate potential vulnerabilities.</li>
<li><em>Use Secure Configuration.</em> Ensure that systems and software are configured securely to prevent unauthorized access and elevation of privilege.</li>
<li><em>Use Security by Design.</em> Incorporate security considerations into the design of systems and software to prevent vulnerabilities from arising in the first place.</li>
</ul>
<h2 class="MuiTypography-root MuiTypography-h2 css-1d8u6kn" id="conclusion" level="2" index="41" siblingcount="55" node="[object Object]">Conclusion</h2>
<p index="42" siblingcount="55">It is important to note that no system can be made completely secure, but by using STRIDE methodologies to identify the threat and implement the appropriate security controls, the risk can be reduced to an acceptable level. In general, to create more secure systems or applications:</p>
<ul>
<li>Encrypt sensitive data, both at rest and in transit to protect them from unauthorized access and tampering.</li>
<li>Implement <a class="MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways css-ir33j0" target="_blank" href="secure-code-training/secure-code-training">Secure coding practices</a> and conduct code reviews using <a class="MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways css-ir33j0" target="_blank" href="https://owasp.org/www-project-top-ten/">OWASP Top 10 Security Risks</a> to identify and remediate potential vulnerabilities.</li>
<li>Validate all input data to ensure that it is coming from a trusted source and that it is in the correct format, to prevent attackers from injecting malicious data.</li>
<li>Regularly monitor your system for suspicious activity and perform regular security testing to identify and address potential vulnerabilities.</li>
<li>Keep software and libraries up to date to ensure that any known vulnerabilities are patched. Train your team about the risks of repudiation and the steps they can take to prevent it.</li>
<li>Regularly assess the security of your systems and networks to identify and address potential vulnerabilities.</li>
</ul>

<h2 class="MuiTypography-root MuiTypography-h2 css-1d8u6kn" id="additional-resources" level="2" index="53" siblingcount="55" node="[object Object]">Additional resources</h2>
<ul>
<li><a class="MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways css-ir33j0" target="_blank" href="secure-code-training">Secure Coding Training</a></li>
<li><a class="MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways css-ir33j0" target="_blank" href="https://owasp.org/www-project-top-ten/">OWASP Top 10 Security Risks</a></li>
<li><a class="MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways css-ir33j0" target="_blank" href="https://github.com/OWASP/DevGuide/blob/master/02-Design/01-Principles%20of%20Security%20Engineering.md">OWASP DEV Guide</a></li>
<li><a class="MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways css-ir33j0" target="_blank" href="https://www.ncsc.gov.uk/collection/cyber-security-design-principles/cyber-security-design-principles">Security Design Principles</a></li>
</ul></div></div>
 </div></div></div></div></section>
