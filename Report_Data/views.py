from django.shortcuts import render,HttpResponse

import pandas as pd
import requests
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from requests.auth import HTTPBasicAuth
import json
from .models import NagraDetails
from urllib.parse import quote
from django.views import View



CACHE_TTL = getattr(settings,'CACHE_TTL', DEFAULT_TIMEOUT)





def all_networks(request):
        http = 'http://172.16.114.74:8080'
        path1   = '/ims/topology/v1/'

        channel_name=''
        product_name=''
        nkey=''
        product_key=''
        service_key=''
        products=''
        n_list=[]
        n_d=[]
        network_url=http+path1+'networks'
        new_session=requests.Session()
        networks_data=new_session.get(network_url).json()

        for net_id in networks_data:
                n_list.append(int(net_id['Key']))
        n_list.sort()
      
        for nid in n_list:
                print(nid)
                get_network_load_url= http+path1+'networks/'+str(nid)+':load'
                print(get_network_load_url)
                dict_get_network=new_session.get(get_network_load_url).json()

                get_channel_url=http+path1+'channels'
                get_channels_data= new_session.get(get_channel_url).json()
                nKey=nid
                for channel_data in get_channels_data:
                       
                        try:
                                        channel_subscriptions=http+path1+'channels/'+'SEC HD_SPORTS'+'/subscriptions'
                                        channel_subscriptions_data=new_session.get(channel_subscriptions)
                                        products=channel_subscriptions_data.json()
                                        print(products)
                                        for products_data in products:
                                                product_key=products_data['ProductKey']
                                                nagra_details.products=product_key
                        except:
                                        product_key=None
               
                bouquet_link_url=http+path1+'networks/'+str(nid)+'/bouquetlinks'
                bouquet_link_data=new_session.get(bouquet_link_url).json()
                for bouquet_link_values in bouquet_link_data:
                        bouquet_id=bouquet_link_values['BouquetKey']
                        
                
                
                delivery_descriptors_url=http+path1+'networks/'+str(nid)+'/deliverydescriptors'
                delivery_descriptors_data=new_session.get(delivery_descriptors_url).json()
                transport_data=[]
                for delivery_descriptors_values in delivery_descriptors_data:
                        transport_data.append(delivery_descriptors_values['TransportKey'])

                
                transport_key_url=http+path1+'transports/'
                transport_key_data=new_session.get(transport_key_url).json()
                for transport_key_values in transport_key_data:
                        transport_id=transport_key_values['TransportStreamId']
                        original_network_id=transport_key_values['OriginalNetworkId']

                        

                service_bouquet_key=[]       
                for transport_key in transport_data:

                        service_key_url=http+path1+'tansports/'+transport_key+'/services'
                        service_key_data=new_session.get(service_key_url).json()
                        for service_key_values in service_key_data:
                                service_key=service_key_values['Key']
                                service_bouquet_link_url=http+path1+'transports/'+transport_key+'/services/'+service_key+'/bouquetLinks'
                                service_bouquet_link_data=new_session.get(service_bouquet_link_url).json()
                                for service_bouquet_link_values in service_bouquet_link_data:
                                        service_bouquet_key=service_bouquet_link_values['Key']
                bouq_key=[]
                bouq_key_url=http+path1+'bouquets/'
                bouq_key_data=new_session.get(bouq_key_url).json()
                for bouq_key_values in bouq_key_data:
                        bouq_id=bouq_key_values['BouquetId']
                        bouq_key.append(bouq_key_values['Key'])
                network_key=[]
                for b_key in bouq_key:
                         network_key_url=http+path1+'bouquets/'+b_key+'/networklinks'
                         network_key_data=new_session.get(network_key_url).json()
                         for network_key_values in network_key_data:
                                network_key.append(network_key_values['NetworkKey'])
                service_key=[]

                for s_key in bouq_key:
                        service_links_url=http+path1+'bouquets/'+s_key+'/servicelinks'
                        service_links_data=new_session.get(service_links_url).json()
                        for service_links_values in service_links_data:
                                service_key.append(service_links_values['ServiceKey'])        
                        nagra_details=NagraDetails()
                        nagra_details.network_id=nid
                        nagra_details.network_name=nid['Name']
                        nagra_details.transport_id=transport_id
                        nagra_details.original_network_id=original_network_id
                        nagra_details.bouquet_id=bouquet_id
                        nagra_details.save()

        return HttpResponse({'status:200'})

               


        
def networks(request):
        http = 'http://172.16.114.74:8080'
        path1   = '/ims/topology/v1/'

        channel_name=''
        product_name=''
        nkey=''
        product_key=''
        service_key=''
        products=''
        n_list=[]
        n_d=[]
        network_url=http+path1+'networks'
        new_session=requests.Session()
        networks_data=new_session.get(network_url).json()
        

        for net_id in networks_data:
                n_list.append(int(net_id['Key']))
        n_list.sort()
      
        for nid in n_list:
                
                print(nid)
                get_network_load_url= http+path1+'networks/'+str(nid)+':load'
                dict_get_network=new_session.get(get_network_load_url).json()

                get_channel_url=http+path1+'channels'
                get_channels_data= new_session.get(get_channel_url).json()
                nKey=nid
                
                for channel_data in get_channels_data:
                        try:            
                                       
                                        print(channel_data['Key'])
                                        
                                        channel_subscriptions=http+path1+'channels/'+channel_data['Key']+'/subscriptions'
                                        channel_subscriptions_data=new_session.get(channel_subscriptions)
                                        products=channel_subscriptions_data.json()
                                        for products_data in products:
                                                product_key=products_data['ProductKey']
                                                print(product_key)
                                                nagra_details=NagraDetails()
                                                nagra_details.network_id=nid
                                                nagra_details.channel_name=channel_data['Key']
                                                nagra_details.products=product_key
                                                nagra_details.save()
                                               
                                                
                                       
                                                
                        except:
                                        product_key=None
                        
                        bouquet_link_url=http+path1+'networks/'+str(nid)+'/bouquetlinks'
                        bouquet_link_data=new_session.get(bouquet_link_url).json()
                        for bouquet_link_values in bouquet_link_data:
                                bouquet_id=bouquet_link_values['BouquetKey']
                                nagra_details.bouquet_id=bouquet_id
                                


                        delivery_descriptors_url=http+path1+'networks/'+str(nid)+'/deliverydescriptors'
                        delivery_descriptors_data=new_session.get(delivery_descriptors_url).json()
                        transport_data=[]
                        for delivery_descriptors_values in delivery_descriptors_data:
                                transport_data.append(delivery_descriptors_values['TransportKey'])
                                
                        transport_key_url=http+path1+'transports/'
                        transport_key_data=new_session.get(transport_key_url).json()
                        for transport_key_values in transport_key_data:
                                transport_id=transport_key_values['TransportStreamId']
                                nagra_details.transport_id=transport_id
                                original_network_id=transport_key_values['OriginalNetworkId']
                                nagra_details.original_network_id=original_network_id
                                

                        service_bouquet_key=[]       
                        for transport_key in transport_data:
                                try:
                                        service_key_url=http+path1+'tansports/'+transport_key+'/services'
                                        service_key_data=new_session.get(service_key_url).json()
                                        for service_key_values in service_key_data:
                                                service_key=service_key_values['Key']
                                except:
                                        service_key=None
                                nagra_details.service_key=service_key
                                
                                
                                try:
                                        service_bouquet_link_url=http+path1+'transports/'+transport_key+'/services/'+service_key+'/bouquetLinks'
                                        service_bouquet_link_data=new_session.get(service_bouquet_link_url).json()
                                        for service_bouquet_link_values in service_bouquet_link_data:
                                                        service_bouquet_key=service_bouquet_link_values['Key']
                                except:

                                        service_bouquet_key=None
                        
                        # bouq_key=[]
                        # try:
                        #         bouq_key_url=http+path1+'bouquets/'
                        #         bouq_key_data=new_session.get(bouq_key_url).json()
                        #         for bouq_key_values in bouq_key_data:
                        #                 bouq_id=bouq_key_values['BouquetId']
                        #                 nagra_details.bouquet_id=bouq_id
                                       
                        #                 bouq_key.append(bouq_key_values['Key'])
                                
                        # except:
                        #         bouq_id=None

                        # network_key=[]
                        # for b_key in bouq_key:
                        #         network_key_url=http+path1+'bouquets/'+b_key+'/networklinks'
                        #         network_key_data=new_session.get(network_key_url).json()
                        #         for network_key_values in network_key_data:
                        #                 network_key.append(network_key_values['NetworkKey'])

                        # service_key=[]
                        # for s_key in bouq_key:
                        #         service_links_url=http+path1+'bouquets/'+s_key+'/servicelinks'
                        #         service_links_data=new_session.get(service_links_url).json()
                        #         for service_links_values in service_links_data:
                        #                 service_key.append(service_links_values['ServiceKey'])  
                                
                                        
        
        return response({'status:200'})





# class ExportImportExcel(APIView):
#         def get (self, request):
#                 student_objs=Student.objects.all()


# def export_excel(request):
#         response= HttpResponse(content_type='application/mx-excel')
#         response['Content-Disposition']= 'attachment; filename=NagraDetails'+\
#                         str(datetime.datetime.now())+'.xls'

#         wb= xlwt.Workbook(encoding='utf-8')
#         ws= wb.add_sheet('NagraDetails')
#         row_num=0
#         font_style=xwlt .XFStyle()
#         font_style.font.bold= True

#       
#         for col_num in range(len(columns)):
#                 ws.write(row_num, col_num, str(row(col_num)), font_style)


def network_load(request):
        http = 'http://172.16.114.74:8080'
        path1   = '/ims/topology/v1/'
        n_list=[]

        network_url=http+path1+'networks'
        new_session=requests.Session()
        networks_data=new_session.get(network_url).json()

        for net_id in networks_data:
                n_list.append(int(net_id['Key']))
        n_list.sort()
        # print(n_list)
        context={
                'http':http,
                'path1':path1
        }
        return HttpResponse({'status:200'})

def get_channels(request):
        http = 'http://172.16.114.74:8080'
        path1   = '/ims/topology/v1/'
        n=network_load(request)
        print(n.text)
        get_channel_url=http+path1+'channels'
        get_channels_data= new_session.get(get_channel_url).json()
        nKey=nid
        for channel_data in get_channels_data:
                       
                        try:
                                        channel_subscriptions=http+path1+'channels/'+'SEC HD_SPORTS'+'/subscriptions'
                                        channel_subscriptions_data=new_session.get(channel_subscriptions)
                                        products=channel_subscriptions_data.json()
                                        print(products)
                                        for products_data in products:
                                                product_key=products_data['ProductKey']
                                                nagra_details.products=product_key
                        except:
                                        product_key=None
        return HttpResponse({'status:200'})
