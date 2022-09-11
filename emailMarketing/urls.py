from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.emailMarketing, name='emailMarketing'),
    url(r'^fetchUsers$', views.fetchUsers, name='fetchUsers'),
    url(r'^enableDisableMarketing$', views.enableDisableMarketing, name='enableDisableMarketing'),
    url(r'^saveConfigureVerify$', views.saveConfigureVerify, name='saveConfigureVerify'),
    url(r'^fetchVerifyLogs$', views.fetchVerifyLogs, name='fetchVerifyLogs'),
    url(r'^(?P<domain>(.*))/emailLists$', views.createEmailList, name='createEmailList'),
    url(r'^submitEmailList$', views.submitEmailList, name='submitEmailList'),
    url(r'^(?P<domain>(.*))/manageLists$', views.manageLists, name='manageLists'),
    url(r'^(?P<domain>(.*))/manageSMTP$', views.manageSMTP, name='manageSMTP'),
    url(r'^(?P<domain>(.*))/configureVerify$', views.configureVerify, name='configureVerify'),
    url(r'^fetchEmails$', views.fetchEmails, name='fetchEmails'),
    url(r'^deleteList$', views.deleteList, name='deleteList'),
    url(r'^emailVerificationJob$', views.emailVerificationJob, name='emailVerificationJob'),
    url(r'^deleteEmail$', views.deleteEmail, name='deleteEmail'),
    url(r'^saveSMTPHost$', views.saveSMTPHost, name='saveSMTPHost'),
    url(r'^fetchSMTPHosts$', views.fetchSMTPHosts, name='fetchSMTPHosts'),
    url(r'^smtpHostOperations$', views.smtpHostOperations, name='smtpHostOperations'),
    url(r'^composeEmailMessage$', views.composeEmailMessage, name='composeEmailMessage'),
    url(r'^saveEmailTemplate$', views.saveEmailTemplate, name='saveEmailTemplate'),
    url(r'^sendEmails$', views.sendEmails, name='sendEmails'),
    url(r'^preview/(?P<templateName>[-\w]+)/$', views.templatePreview, name='templatePreview'),
    url(r'^fetchJobs$', views.fetchJobs, name='fetchJobs'),
    url(r'^startEmailJob$', views.startEmailJob, name='startEmailJob'),
    url(r'^deleteTemplate$', views.deleteTemplate, name='deleteTemplate'),
    url(r'^deleteJob$', views.deleteJob, name='deleteJob'),
    url(r'^remove/(?P<listName>[-\w]+)/(?P<emailAddress>\w+@.+)$', views.remove, name='remove'),
]