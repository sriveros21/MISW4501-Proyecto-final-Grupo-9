package com.example.sportapp.data.repository

import com.example.sportapp.data.api.CalculateFTPVo2Service
import com.example.sportapp.data.api.EventsService
import com.example.sportapp.data.model.SessionIdRequest
import com.example.sportapp.data.model.TrainingMetricsCalculatedResponse
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.RequestBody.Companion.toRequestBody
import retrofit2.Callback


class DataRepository(private val apiService: EventsService) {
    fun getCalendarEvents(userId: Int) = apiService.getCalendarEvents(userId)
}

class FTPVO2Repository(private val ftpVo2Service: CalculateFTPVo2Service) {
    fun postCalculateFTPVo2(sessionId: Int, callback: Callback<TrainingMetricsCalculatedResponse>) {
        val sessionIdRequest = SessionIdRequest(sessionId)
        val requestBody = sessionIdRequest.toString().toRequestBody("application/json".toMediaTypeOrNull())
        ftpVo2Service.postCalculateFTPVo2Service(requestBody).enqueue(callback)
    }
}