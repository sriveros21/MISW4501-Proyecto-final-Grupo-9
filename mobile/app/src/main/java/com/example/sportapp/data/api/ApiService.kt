package com.example.sportapp.data.api

import com.example.sportapp.data.model.CalendarEvent
import retrofit2.Call
import retrofit2.http.GET
import retrofit2.http.Path


interface EventsService {
    @GET("user/{userId}/calendar")
    //@GET("/user/1/calendar")
    fun getCalendarEvents(@Path("userId") userId: Int): Call<List<CalendarEvent>>
}


interface ApiService {
    @GET("user/{userId}/calendar")
    //@GET("/user/1/calendar")
    fun getCalendarEvents(@Path("userId") userId: Int): Call<List<CalendarEvent>>
}
