package com.example.sportapp.data.api

import com.example.sportapp.data.model.CalendarEvent
import com.example.sportapp.data.model.TrainingMetricsCalculatedResponse
import okhttp3.RequestBody
import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.Path


interface EventsService {
    @GET("user/{userId}/calendar")
    //@GET("/user/1/calendar")
    fun getCalendarEvents(@Path("userId") userId: Int): Call<List<CalendarEvent>>
}

interface CalculateFTPVo2Service {
    @POST("/calculate-ftp-vo2max")
    fun postCalculateFTPVo2Service(@Body requestBody: RequestBody): Call<TrainingMetricsCalculatedResponse>
}


//interface ApiService {
//    @GET("user/{userId}/calendar")
//    //@GET("/user/1/calendar")
//    fun getCalendarEvents(@Path("userId") userId: Int): Call<List<CalendarEvent>>
//}
