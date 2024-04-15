package com.example.sportapp.data.model

import com.google.gson.annotations.SerializedName

data class TrainingMetricsCalculatedResponse (
    val ftp: Double,
    val vo2max: Double
)

data class SessionIdRequest(
    @SerializedName("session_id") val sessionId: String
)



