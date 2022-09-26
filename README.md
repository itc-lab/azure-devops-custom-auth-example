# Azure DevOps Pileline and Custom authentication in Azure Static Web Apps Example

Azure DevOps の Pileline を使って Azure Static Web Apps にデプロイできる Example です。  
デプロイしたアプリは、Azure Static Web Apps でのカスタム認証 で Azure AD の一つのテナントに対して認証機能をテストできます。

フロントエンドは、TypeScript で記述された React ベースの SPA (Single-Page App) です。  
`api/hello/` は、Python の API です。認証されたユーザーのユーザー名をレスポンスします。  
また、
`X-MS-CLIENT-PRINCIPAL-ID`  
`X-MS-CLIENT-PRINCIPAL-NAME`  
`X-MS-CLIENT-PRINCIPAL-IDP`  
`X-MS-CLIENT-PRINCIPAL`  
`X-MS-TOKEN-AAD-ID-TOKEN`  
`X-MS-TOKEN-AAD-ACCESS-TOKEN`  
`X-MS-TOKEN-AAD-REFRESH-TOKEN`  
ヘッダの値も表示します。

This is an example that can be deployed to Azure Static Web Apps using Pileline in Azure DevOps.  
Deployed apps can test authentication functionality against a single Azure AD tenant with Custom authentication in Azure Static Web Apps.

The frontend is a React-based SPA (Single-Page App) written in TypeScript.  
`api/hello/` is a Python API that returns a message that contains the authenticated user name.  
It also displays the values of the following headers:  
`X-MS-CLIENT-PRINCIPAL-ID`  
`X-MS-CLIENT-PRINCIPAL-NAME`  
`X-MS-CLIENT-PRINCIPAL-IDP`  
`X-MS-CLIENT-PRINCIPAL`  
`X-MS-TOKEN-AAD-ID-TOKEN`  
`X-MS-TOKEN-AAD-ACCESS-TOKEN`  
`X-MS-TOKEN-AAD-REFRESH-TOKEN`