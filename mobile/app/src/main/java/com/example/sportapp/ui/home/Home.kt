package com.example.sportapp.ui.home

import android.content.Intent
import android.os.Bundle
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity
import com.example.sportapp.R
import com.example.sportapp.ui.views.StravaViewConnect

class Home : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_home)
        // String appName = getString(R.string.app_name)
        val btnStrava = findViewById<ImageView>(R.id.imgStrava)


        //Redirige a la Actividad Strava.
        btnStrava.setOnClickListener{
            val strava = Intent(this, StravaViewConnect::class.java)
            startActivity(strava)
        }
    }


}