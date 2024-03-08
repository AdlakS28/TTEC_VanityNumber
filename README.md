# TTEC_VanityNumber
Phone numbers to vanity numbers conversion implementation in Amazon Connect using Amazon Lambda and Amazon DynamoDB.

# Working Amazon Connect phone number to test in my environment: +1 678-7998-708

# Reasoning for implementing the solution
      1. The primary objective is to convert phone numbers to vanity numbers. This is a common request in any businesses to seek memorable   phone numbers for branding purposes. By converting phone numbers to vanity numbers, businesses can increase the likelihood of customers remembering and contacting them.
      
      2. Since the number of possible vanity numbers can be large, it's essential to select the best ones. The scoring mechanism allows us to evaluate and rank vanity numbers based on certain criteria. In the provided implementation, I have used a simple scoring based on the length of the vanity number, where shorter vanity numbers are considered better. However, in a real-world scenario, more sophisticated scoring methods could be employed, considering factors like ease of pronunciation, relevance to the business, or memorable word combinations.

# What shortcuts did you take that would be a bad practice in production
      I have not used the shortcut but due to time limitation I have not done the exception handling properly. 

# What would you have done with more time? We know you have a like ?
      I would have implemanted in more better way, I thought of integrating Gen AI service to get best vanity number and do the proper exception handling. 

# What other considerations would you make before making our toy app into something that would be ready for high volumes of traffic, potential attacks from bad folks, etc. -
    # **Scalability:** Ensure that the system can scale horizontally to handle increasing loads. This involves optimizing code for performance, leveraging managed services like AWS Lambda, API Gateway, and DynamoDB Auto Scaling to handle spikes in traffic, and implementing caching mechanisms where applicable to reduce the load on backend systems.

    # **Resilience:** Design the system with fault tolerance in mind. Implement retry mechanisms for failed requests, use AWS services like AWS Lambda and DynamoDB that are designed for high availability, and deploy the application across multiple Availability Zones to minimize the impact of outages.

    # **Security:** Harden the application against potential attacks by implementing security best practices. This includes enforcing HTTPS for communication, implementing proper authentication and authorization mechanisms, sanitizing input to prevent injection attacks, and regularly patching and updating dependencies to address security vulnerabilities.

    # **Compliance and Regulations:** Ensure compliance with relevant regulations such as GDPR, HIPAA, or PCI DSS, depending on the nature of the application and the data it handles. Implement appropriate data encryption, access controls, and audit trails to meet regulatory requirements.

# Rrchitecture diagram

      ![image](https://github.com/AdlakS28/TTEC_VanityNumber/assets/aqrchitecture diagram.JPG)


# Deployment Instructions


