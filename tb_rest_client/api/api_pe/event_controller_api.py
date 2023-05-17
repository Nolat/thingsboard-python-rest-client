# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0PE
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class EventControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def clear_events_using_post(self, entity_type, entity_id, **kwargs):  # noqa: E501
        """Clear Events (clearEvents)  # noqa: E501

        Clears events by filter for specified entity.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clear_events_using_post(entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
        :param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param EventFilter body:
        :param int start_time: Timestamp. Events with creation time before it won't be queried.
        :param int end_time: Timestamp. Events with creation time after it won't be queried.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.clear_events_using_post_with_http_info(entity_type, entity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.clear_events_using_post_with_http_info(entity_type, entity_id, **kwargs)  # noqa: E501
            return data

    def clear_events_using_post_with_http_info(self, entity_type, entity_id, **kwargs):  # noqa: E501
        """Clear Events (clearEvents)  # noqa: E501

        Clears events by filter for specified entity.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clear_events_using_post_with_http_info(entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
        :param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param EventFilter body:
        :param int start_time: Timestamp. Events with creation time before it won't be queried.
        :param int end_time: Timestamp. Events with creation time after it won't be queried.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'body', 'start_time', 'end_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clear_events_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `clear_events_using_post`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `clear_events_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501

        query_params = []
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501

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
            '/api/events/{entityType}/{entityId}/clear{?endTime,startTime}', 'POST',
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

    def get_events_using_get(self, entity_type, entity_id, tenant_id, page_size, page, **kwargs):  # noqa: E501
        """Get Events (Deprecated)  # noqa: E501

        Returns a page of events for specified entity. Deprecated and will be removed in next minor release. The call was deprecated to improve the performance of the system. Current implementation will return 'Lifecycle' events only. Use 'Get events by type' or 'Get events by filter' instead. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_events_using_get(entity_type, entity_id, tenant_id, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
        :param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param str tenant_id: A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str text_search: The value is not used in searching.
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :param int start_time: Timestamp. Events with creation time before it won't be queried.
        :param int end_time: Timestamp. Events with creation time after it won't be queried.
        :return: PageDataEventInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_events_using_get_with_http_info(entity_type, entity_id, tenant_id, page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_events_using_get_with_http_info(entity_type, entity_id, tenant_id, page_size, page, **kwargs)  # noqa: E501
            return data

    def get_events_using_get_with_http_info(self, entity_type, entity_id, tenant_id, page_size, page, **kwargs):  # noqa: E501
        """Get Events (Deprecated)  # noqa: E501

        Returns a page of events for specified entity. Deprecated and will be removed in next minor release. The call was deprecated to improve the performance of the system. Current implementation will return 'Lifecycle' events only. Use 'Get events by type' or 'Get events by filter' instead. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_events_using_get_with_http_info(entity_type, entity_id, tenant_id, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
        :param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param str tenant_id: A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str text_search: The value is not used in searching.
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :param int start_time: Timestamp. Events with creation time before it won't be queried.
        :param int end_time: Timestamp. Events with creation time after it won't be queried.
        :return: PageDataEventInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'tenant_id', 'page_size', 'page', 'text_search', 'sort_property', 'sort_order', 'start_time', 'end_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_events_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `get_events_using_get`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `get_events_using_get`")  # noqa: E501
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params or
                params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `get_events_using_get`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_events_using_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_events_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501

        query_params = []
        if 'tenant_id' in params:
            query_params.append(('tenantId', params['tenant_id']))  # noqa: E501
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
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501

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
            '/api/events/{entityType}/{entityId}{?endTime,page,pageSize,sortOrder,sortProperty,startTime,tenantId,textSearch}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataEventInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_events_using_get1(self, entity_type, entity_id, event_type, tenant_id, page_size, page, **kwargs):  # noqa: E501
        """Get Events by type (getEvents)  # noqa: E501

        Returns a page of events for specified entity by specifying event type. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_events_using_get1(entity_type, entity_id, event_type, tenant_id, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
        :param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param str event_type: A string value representing event type (required)
        :param str tenant_id: A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str text_search: The value is not used in searching.
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :param int start_time: Timestamp. Events with creation time before it won't be queried.
        :param int end_time: Timestamp. Events with creation time after it won't be queried.
        :return: PageDataEventInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_events_using_get1_with_http_info(entity_type, entity_id, event_type, tenant_id, page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_events_using_get1_with_http_info(entity_type, entity_id, event_type, tenant_id, page_size, page, **kwargs)  # noqa: E501
            return data

    def get_events_using_get1_with_http_info(self, entity_type, entity_id, event_type, tenant_id, page_size, page, **kwargs):  # noqa: E501
        """Get Events by type (getEvents)  # noqa: E501

        Returns a page of events for specified entity by specifying event type. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_events_using_get1_with_http_info(entity_type, entity_id, event_type, tenant_id, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
        :param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param str event_type: A string value representing event type (required)
        :param str tenant_id: A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str text_search: The value is not used in searching.
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :param int start_time: Timestamp. Events with creation time before it won't be queried.
        :param int end_time: Timestamp. Events with creation time after it won't be queried.
        :return: PageDataEventInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'event_type', 'tenant_id', 'page_size', 'page', 'text_search', 'sort_property', 'sort_order', 'start_time', 'end_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_events_using_get1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `get_events_using_get1`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `get_events_using_get1`")  # noqa: E501
        # verify the required parameter 'event_type' is set
        if ('event_type' not in params or
                params['event_type'] is None):
            raise ValueError("Missing the required parameter `event_type` when calling `get_events_using_get1`")  # noqa: E501
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params or
                params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `get_events_using_get1`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_events_using_get1`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_events_using_get1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501
        if 'event_type' in params:
            path_params['eventType'] = params['event_type']  # noqa: E501

        query_params = []
        if 'tenant_id' in params:
            query_params.append(('tenantId', params['tenant_id']))  # noqa: E501
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
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501

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
            '/api/events/{entityType}/{entityId}/{eventType}{?endTime,page,pageSize,sortOrder,sortProperty,startTime,tenantId,textSearch}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataEventInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_events_using_post(self, tenant_id, page_size, page, entity_type, entity_id, **kwargs):  # noqa: E501
        """Get Events by event filter (getEvents)  # noqa: E501

        Returns a page of events for the chosen entity by specifying the event filter. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # Event Filter Definition  5 different eventFilter objects could be set for different event types. The eventType field is required. Others are optional. If some of them are set, the filtering will be applied according to them. See the examples below for all the fields used for each event type filtering.   Note,   * 'server' - string value representing the server name, identifier or ip address where the platform is running;  * 'errorStr' - the case insensitive 'contains' filter based on error message.  ## Error Event Filter  ```json {    \"eventType\":\"ERROR\",    \"server\":\"ip-172-31-24-152\",    \"method\":\"onClusterEventMsg\",    \"errorStr\":\"Error Message\" } ```   * 'method' - string value representing the method name when the error happened.  ## Lifecycle Event Filter  ```json {    \"eventType\":\"LC_EVENT\",    \"server\":\"ip-172-31-24-152\",    \"event\":\"STARTED\",    \"status\":\"Success\",    \"errorStr\":\"Error Message\" } ```   * 'event' - string value representing the lifecycle event type;  * 'status' - string value representing status of the lifecycle event.  ## Statistics Event Filter  ```json {    \"eventType\":\"STATS\",    \"server\":\"ip-172-31-24-152\",    \"messagesProcessed\":10,    \"errorsOccurred\":5 } ```   * 'messagesProcessed' - the minimum number of successfully processed messages;  * 'errorsOccurred' - the minimum number of errors occurred during messages processing.  ## Debug Rule Node Event Filter  ```json {    \"eventType\":\"DEBUG_RULE_NODE\",    \"msgDirectionType\":\"IN\",    \"server\":\"ip-172-31-24-152\",    \"dataSearch\":\"humidity\",    \"metadataSearch\":\"deviceName\",    \"entityName\":\"DEVICE\",    \"relationType\":\"Success\",    \"entityId\":\"de9d54a0-2b7a-11ec-a3cc-23386423d98f\",    \"msgType\":\"POST_TELEMETRY_REQUEST\",    \"isError\":\"false\",    \"errorStr\":\"Error Message\" } ```  ## Debug Rule Chain Event Filter  ```json {    \"eventType\":\"DEBUG_RULE_CHAIN\",    \"msgDirectionType\":\"IN\",    \"server\":\"ip-172-31-24-152\",    \"dataSearch\":\"humidity\",    \"metadataSearch\":\"deviceName\",    \"entityName\":\"DEVICE\",    \"relationType\":\"Success\",    \"entityId\":\"de9d54a0-2b7a-11ec-a3cc-23386423d98f\",    \"msgType\":\"POST_TELEMETRY_REQUEST\",    \"isError\":\"false\",    \"errorStr\":\"Error Message\" } ```   * 'msgDirectionType' - string value representing msg direction type (incoming to entity or outcoming from entity);  * 'dataSearch' - the case insensitive 'contains' filter based on data (key and value) for the message;  * 'metadataSearch' - the case insensitive 'contains' filter based on metadata (key and value) for the message;  * 'entityName' - string value representing the entity type;  * 'relationType' - string value representing the type of message routing;  * 'entityId' - string value representing the entity id in the event body (originator of the message);  * 'msgType' - string value representing the message type;  * 'isError' - boolean value to filter the errors.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_events_using_post(tenant_id, page_size, page, entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
        :param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param EventFilter body:
        :param str text_search: The value is not used in searching.
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :param int start_time: Timestamp. Events with creation time before it won't be queried.
        :param int end_time: Timestamp. Events with creation time after it won't be queried.
        :return: PageDataEventInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_events_using_post_with_http_info(tenant_id, page_size, page, entity_type, entity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_events_using_post_with_http_info(tenant_id, page_size, page, entity_type, entity_id, **kwargs)  # noqa: E501
            return data

    def get_events_using_post_with_http_info(self, tenant_id, page_size, page, entity_type, entity_id, **kwargs):  # noqa: E501
        """Get Events by event filter (getEvents)  # noqa: E501

        Returns a page of events for the chosen entity by specifying the event filter. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # Event Filter Definition  5 different eventFilter objects could be set for different event types. The eventType field is required. Others are optional. If some of them are set, the filtering will be applied according to them. See the examples below for all the fields used for each event type filtering.   Note,   * 'server' - string value representing the server name, identifier or ip address where the platform is running;  * 'errorStr' - the case insensitive 'contains' filter based on error message.  ## Error Event Filter  ```json {    \"eventType\":\"ERROR\",    \"server\":\"ip-172-31-24-152\",    \"method\":\"onClusterEventMsg\",    \"errorStr\":\"Error Message\" } ```   * 'method' - string value representing the method name when the error happened.  ## Lifecycle Event Filter  ```json {    \"eventType\":\"LC_EVENT\",    \"server\":\"ip-172-31-24-152\",    \"event\":\"STARTED\",    \"status\":\"Success\",    \"errorStr\":\"Error Message\" } ```   * 'event' - string value representing the lifecycle event type;  * 'status' - string value representing status of the lifecycle event.  ## Statistics Event Filter  ```json {    \"eventType\":\"STATS\",    \"server\":\"ip-172-31-24-152\",    \"messagesProcessed\":10,    \"errorsOccurred\":5 } ```   * 'messagesProcessed' - the minimum number of successfully processed messages;  * 'errorsOccurred' - the minimum number of errors occurred during messages processing.  ## Debug Rule Node Event Filter  ```json {    \"eventType\":\"DEBUG_RULE_NODE\",    \"msgDirectionType\":\"IN\",    \"server\":\"ip-172-31-24-152\",    \"dataSearch\":\"humidity\",    \"metadataSearch\":\"deviceName\",    \"entityName\":\"DEVICE\",    \"relationType\":\"Success\",    \"entityId\":\"de9d54a0-2b7a-11ec-a3cc-23386423d98f\",    \"msgType\":\"POST_TELEMETRY_REQUEST\",    \"isError\":\"false\",    \"errorStr\":\"Error Message\" } ```  ## Debug Rule Chain Event Filter  ```json {    \"eventType\":\"DEBUG_RULE_CHAIN\",    \"msgDirectionType\":\"IN\",    \"server\":\"ip-172-31-24-152\",    \"dataSearch\":\"humidity\",    \"metadataSearch\":\"deviceName\",    \"entityName\":\"DEVICE\",    \"relationType\":\"Success\",    \"entityId\":\"de9d54a0-2b7a-11ec-a3cc-23386423d98f\",    \"msgType\":\"POST_TELEMETRY_REQUEST\",    \"isError\":\"false\",    \"errorStr\":\"Error Message\" } ```   * 'msgDirectionType' - string value representing msg direction type (incoming to entity or outcoming from entity);  * 'dataSearch' - the case insensitive 'contains' filter based on data (key and value) for the message;  * 'metadataSearch' - the case insensitive 'contains' filter based on metadata (key and value) for the message;  * 'entityName' - string value representing the entity type;  * 'relationType' - string value representing the type of message routing;  * 'entityId' - string value representing the entity id in the event body (originator of the message);  * 'msgType' - string value representing the message type;  * 'isError' - boolean value to filter the errors.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_events_using_post_with_http_info(tenant_id, page_size, page, entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
        :param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param EventFilter body:
        :param str text_search: The value is not used in searching.
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :param int start_time: Timestamp. Events with creation time before it won't be queried.
        :param int end_time: Timestamp. Events with creation time after it won't be queried.
        :return: PageDataEventInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'page_size', 'page', 'entity_type', 'entity_id', 'body', 'text_search', 'sort_property', 'sort_order', 'start_time', 'end_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_events_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params or
                params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `get_events_using_post`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_events_using_post`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_events_using_post`")  # noqa: E501
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `get_events_using_post`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `get_events_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501

        query_params = []
        if 'tenant_id' in params:
            query_params.append(('tenantId', params['tenant_id']))  # noqa: E501
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
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501

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
            '/api/events/{entityType}/{entityId}{?endTime,page,pageSize,sortOrder,sortProperty,startTime,tenantId,textSearch}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataEventInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
