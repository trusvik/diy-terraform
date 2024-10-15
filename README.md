# Fix it yourself lab

Du kan gjøre denne Laben på egen maskin eller i Cloud 9. Hvis du ghør den på egen maskin trenger du

* AWS CLI
* Terraform
* AWS IAM nøkler for din bruker

## Beksrivelse 

Lambdafunksjonen i dette repositoryiet kan ikke deployes og virker ikke av et par årsaker.

* Rollenavn er hardkodet, det finnes rolle med samme navn fra før.
* Lambdafunksjonen sin Rolle gir ikke tilgang til S3
* Navnet til lambdafunksjonen er hardkodet.
* Funksjonene forventer å finne en environment variabel som heter ```BUCKET_NAME```     
```
bucket_name = os.environ['BUCKET_NAME'] 
```
* Les dokumentasjonen til aws_lambda_function resource, og finn ut av hvordan du kan sende inn en "environment" variabel til lambda-funksjonen siden den forventer det.
  https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function.html

## Oppgave

Få koden til å kjøre, og forbedre koden ved å innføre Terrafomr variabler.





