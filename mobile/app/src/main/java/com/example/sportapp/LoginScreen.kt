package com.example.sportapp

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import com.example.sportapp.ui.home.Home

class LoginScreen : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)
        // String appName = getString(R.string.app_name)

        val btnLoginE = findViewById<Button>(R.id.btnLogin)


        //Redirige a la Actividad Home.
        btnLoginE.setOnClickListener {
            val home = Intent(this, Home::class.java)
            startActivity(home)
        }

        // Ponemos VALORES por defecto usuario en 1. mientras se hace HU Login.
        SportApp.userCodeId = 1
        SportApp.powerOutput = 250
        SportApp.maxHeartRate= 180
        SportApp.restingHeartRate = 60

    }
}
