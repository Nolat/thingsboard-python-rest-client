# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class QueueControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_queue_using_delete(self, queue_id, **kwargs):  # noqa: E501
        """Delete Queue (deleteQueue)  # noqa: E501

        Deletes the Queue.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_queue_using_delete(queue_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str queue_id: A string value representing the queue id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_queue_using_delete_with_http_info(queue_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_queue_using_delete_with_http_info(queue_id, **kwargs)  # noqa: E501
            return data

    def delete_queue_using_delete_with_http_info(self, queue_id, **kwargs):  # noqa: E501
        """Delete Queue (deleteQueue)  # noqa: E501

        Deletes the Queue.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_queue_using_delete_with_http_info(queue_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str queue_id: A string value representing the queue id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_queue_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params or
                params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `delete_queue_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/queues/{queueId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_queue_by_id_using_get(self, queue_id, **kwargs):  # noqa: E501
        """Get Queue (getQueueById)  # noqa: E501

        Fetch the Queue object based on the provided Queue Id.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_queue_by_id_using_get(queue_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str queue_id: A string value representing the queue id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: Queue
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_queue_by_id_using_get_with_http_info(queue_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_queue_by_id_using_get_with_http_info(queue_id, **kwargs)  # noqa: E501
            return data

    def get_queue_by_id_using_get_with_http_info(self, queue_id, **kwargs):  # noqa: E501
        """Get Queue (getQueueById)  # noqa: E501

        Fetch the Queue object based on the provided Queue Id.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_queue_by_id_using_get_with_http_info(queue_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str queue_id: A string value representing the queue id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: Queue
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_queue_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'queue_id' is set
        if ('queue_id' not in params or
                params['queue_id'] is None):
            raise ValueError("Missing the required parameter `queue_id` when calling `get_queue_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'queue_id' in params:
            path_params['queueId'] = params['queue_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/queues/{queueId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Queue',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_queue_by_name_using_get(self, queue_name, **kwargs):  # noqa: E501
        """Get Queue (getQueueByName)  # noqa: E501

        Fetch the Queue object based on the provided Queue name.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_queue_by_name_using_get(queue_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str queue_name: A string value representing the queue id. For example, 'Main' (required)
        :return: Queue
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_queue_by_name_using_get_with_http_info(queue_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_queue_by_name_using_get_with_http_info(queue_name, **kwargs)  # noqa: E501
            return data

    def get_queue_by_name_using_get_with_http_info(self, queue_name, **kwargs):  # noqa: E501
        """Get Queue (getQueueByName)  # noqa: E501

        Fetch the Queue object based on the provided Queue name.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_queue_by_name_using_get_with_http_info(queue_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str queue_name: A string value representing the queue id. For example, 'Main' (required)
        :return: Queue
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_queue_by_name_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'queue_name' is set
        if ('queue_name' not in params or
                params['queue_name'] is None):
            raise ValueError("Missing the required parameter `queue_name` when calling `get_queue_by_name_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'queue_name' in params:
            path_params['queueName'] = params['queue_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/queues/name/{queueName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Queue',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tenant_queues_by_service_type_using_get(self, service_type, page_size, page, **kwargs):  # noqa: E501
        """Get Queues (getTenantQueuesByServiceType)  # noqa: E501

        Returns a page of queues registered in the platform. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tenant_queues_by_service_type_using_get(service_type, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service_type: Service type (implemented only for the TB-RULE-ENGINE) (required)
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str text_search: The case insensitive 'substring' filter based on the queue name.
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :return: PageDataQueue
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tenant_queues_by_service_type_using_get_with_http_info(service_type, page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tenant_queues_by_service_type_using_get_with_http_info(service_type, page_size, page, **kwargs)  # noqa: E501
            return data

    def get_tenant_queues_by_service_type_using_get_with_http_info(self, service_type, page_size, page, **kwargs):  # noqa: E501
        """Get Queues (getTenantQueuesByServiceType)  # noqa: E501

        Returns a page of queues registered in the platform. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tenant_queues_by_service_type_using_get_with_http_info(service_type, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service_type: Service type (implemented only for the TB-RULE-ENGINE) (required)
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str text_search: The case insensitive 'substring' filter based on the queue name.
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :return: PageDataQueue
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['service_type', 'page_size', 'page', 'text_search', 'sort_property', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tenant_queues_by_service_type_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'service_type' is set
        if ('service_type' not in params or
                params['service_type'] is None):
            raise ValueError("Missing the required parameter `service_type` when calling `get_tenant_queues_by_service_type_using_get`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_tenant_queues_by_service_type_using_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_tenant_queues_by_service_type_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'service_type' in params:
            query_params.append(('serviceType', params['service_type']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/queues{?page,pageSize,serviceType,sortOrder,sortProperty,textSearch}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataQueue',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_queue_using_post(self, service_type, **kwargs):  # noqa: E501
        """Create Or Update Queue (saveQueue)  # noqa: E501

        Create or update the Queue. When creating queue, platform generates Queue Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). Specify existing Queue id to update the queue. Referencing non-existing Queue Id will cause 'Not Found' error.  Queue name is unique in the scope of sysadmin. Remove 'id', 'tenantId' from the request body example (below) to create new Queue entity.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_queue_using_post(service_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service_type: Service type (implemented only for the TB-RULE-ENGINE) (required)
        :param Queue body:
        :return: Queue
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_queue_using_post_with_http_info(service_type, **kwargs)  # noqa: E501
        else:
            (data) = self.save_queue_using_post_with_http_info(service_type, **kwargs)  # noqa: E501
            return data

    def save_queue_using_post_with_http_info(self, service_type, **kwargs):  # noqa: E501
        """Create Or Update Queue (saveQueue)  # noqa: E501

        Create or update the Queue. When creating queue, platform generates Queue Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). Specify existing Queue id to update the queue. Referencing non-existing Queue Id will cause 'Not Found' error.  Queue name is unique in the scope of sysadmin. Remove 'id', 'tenantId' from the request body example (below) to create new Queue entity.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_queue_using_post_with_http_info(service_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service_type: Service type (implemented only for the TB-RULE-ENGINE) (required)
        :param Queue body:
        :return: Queue
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['service_type', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_queue_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'service_type' is set
        if ('service_type' not in params or
                params['service_type'] is None):
            raise ValueError("Missing the required parameter `service_type` when calling `save_queue_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'service_type' in params:
            query_params.append(('serviceType', params['service_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/queues{?serviceType}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Queue',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
