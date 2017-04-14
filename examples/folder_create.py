import FuelSDK as fsdk
#from FuelSDK import client
# import ET_Client
# myclient = ET_Client.ET_Client()
params = {
    'clientid': '',
    'clientsecret': '',
    'appsignature': 'none',
    'defaultwsdl': 'https://webservice.exacttarget.com/etframework.wsdl',
    'authenticationurl': 'https://auth.exacttargetapis.com/v1/requestToken?legacy=1',
    'wsdl_file_local_loc': '/tmp/ExactTargetWSDL.s6.xml',
}
myclient = fsdk.ET_Client(params=params)

print('authToken: {}'.format(myclient.authToken))
print('internalAuthToken: {}'.format(myclient.internalAuthToken))
print('authTokenExpiration: {}'.format(myclient.authTokenExpiration))

folder = fsdk.ET_Folder()
folder.auth_stub = myclient

folder_name = 'SDKExampleFolder01'
folder.props = {
    'CustomerKey': folder_name,
    'Name': folder_name,
    'Description': folder_name,
    'ContentType': 'asset',
    'ParentFolder': {'ID': '852737'},
    'AllowChildren': 'true',
    'IsEditable': 'true',
}
results = folder.post()
print('*' * 33)
print('code {}'.format(results.code))
print('status {}'.format(results.status))
print('message {}'.format(results.message))
print('request_id {}'.format(results.request_id))
print('more_results {}'.format(results.more_results))
print('results {}'.format(results.results))
