Selenium and ChromeDriver to 
1. Login into NS
2. Choose a role/account
3. Navigate to Suitelet Deployment
4. Update Translation tab (WIP)

Create a file at `data/login.json`

```
{
	"url": <login page>,
	"user": <user ID / email>,
	"pass": "",
	"answer": <security question>,

	"account_id_qa_bundler": "",
	"deployment_id_qa_bundler_ei_prefs": ,
	"xp_account_qa_bundler": "",
	
	"account_id_ss2_test": <account ID>,
	"deployment_id_ss2_bundler_ei_prefs": <internal ID of deployment>,
	"xp_account_my_ss2_ac": <xpath of your account on choose account page>
}
```
