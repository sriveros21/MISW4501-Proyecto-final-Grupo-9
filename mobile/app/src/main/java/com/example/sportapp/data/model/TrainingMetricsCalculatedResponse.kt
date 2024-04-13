package com.example.sportapp.data.model

import com.google.gson.annotations.SerializedName

data class TrainingMetricsCalculatedResponse (
    val type: String,
    val data: TrainingMetricsData
)

data class TrainingMetricsData(
    val session_id: String,
    val user_id: Int,
    val ftp: Double,
    val vo2max: Double,
    val timestamp: String
)

data class SessionIdRequest(
    @SerializedName("session_id") val sessionId: Int
)