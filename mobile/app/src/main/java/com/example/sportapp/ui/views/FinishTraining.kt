package com.example.sportapp.ui.views

import android.content.Intent
import android.icu.text.SimpleDateFormat
import android.os.Bundle
import android.widget.ImageView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.example.sportapp.R
import com.example.sportapp.ui.home.Home
import java.util.Date
import java.util.Locale

class FinishTraining : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_finish_training)

        val ivHome = findViewById<ImageView>(R.id.ivHome)
        val ivRunExe = findViewById<ImageView>(R.id.ivRunExe)

        //Variables de la vista
        val tvwTypeRun = findViewById<TextView>(R.id.tvwType)
        val tvwTimeTotal = findViewById<TextView>(R.id.tvwTimeTotal)
        val tvwDateTraining = findViewById<TextView>(R.id.tvwDateTraining)
        val tvwCalTraining = findViewById<TextView>(R.id.tvwCalTraining)
        val tvwFTP = findViewById<TextView>(R.id.tvwFTP)
        val tvwVO2 = findViewById<TextView>(R.id.tvwVO2)

        ivHome.setOnClickListener{
            val home = Intent(this, Home::class.java)
            startActivity(home)
        }

        ivRunExe.setOnClickListener{
            val home = Intent(this, StartTraining::class.java)
            startActivity(home)
        }


        val timeTraining = intent.getStringExtra("timeTraining").toString()
        val valorTraining = intent.getStringExtra("valorTraining").toString()

        tvwTypeRun.text = tvwTypeRun.text.toString() + " " +  valorTraining
        tvwTimeTotal.text = tvwTimeTotal.text.toString() + " " + timeTraining
        tvwDateTraining.text = tvwDateTraining.text.toString() + " " + SimpleDateFormat("dd/MM/yyyy", Locale.getDefault()).format(Date())
        tvwCalTraining.text = tvwCalTraining.text.toString() + " " + "500 kCal"
        tvwFTP.text = tvwFTP.text.toString() + " " + "238 vatios"
        tvwVO2.text = tvwVO2.text.toString() + " " + "60 ml/kg/min"

    }
}