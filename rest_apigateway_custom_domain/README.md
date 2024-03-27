# Rest Apigateway with custom domain

*With this template you can deploy an Amazon API Gateway REST API endpoint with a simple public HTTP endpoint integration.*

### Requirements
* *AWS Sam CLI*  - [Install Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
* *ACM Certificate issued asociated to your domain*  [Certificate Manager AWS](https://aws.amazon.com/es/certificate-manager/?nc=sn&loc=1)
* *DNS Hosted Zone* For this example we use a DNS Hosted zone in AWS, but you can use your own preference DNS manager

### Validate SAM Template
* In the console you can verify if the template is linted and valid **``` sam validate --lint ```** to avoid any lint error or missing configuration in your template

### Input Variables
* **HttpUrl**: Reffers to the URL of your backend system that will be the integration of the apigateway in the different methods
* **ACMCertificateArn**: Reffers to the ARN of the certificate that you will need to create the custom domain associated to the apigateway
* **CustomDomainName**: This is the domain or subdomain for your apigateway
* **CustomHostedZoneId**: This is a parameter that is provided when you register a domain in AWS - [Hosted Zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-working-with.html)

### Build and Deploy SAM Template

* Clone this repository or copy this template, then execute **``` sam build ```** in the terminal

This command creates the artifacts and the template that will be deployed

### Deploy SAM Template

* Deploying this template with **``` sam deploy ```**  or with **```sam deploy --guided```** will create a Rest Apigateway with a method GET configured with custom URL as a parameter

> [!NOTE]
> If you use the --guided you will see something like this, and must provide some information to get a successfully deployment

![Screenshot](deploy.png)

* During deployment you will get the output of the resources that will be created in your stack

### Test your resources
When the deployment gets finished you will see in console your defined outputs and you can go to the AWS Console to verify and test your resources

![Screenshot](outputs.png)

![Screenshot](cloud.png)

> [!WARNING]
> Remember to delete your cloud resources if you don't need it to avoid additional costs using **``` sam delete ```**
