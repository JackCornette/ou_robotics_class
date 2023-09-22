;; Auto-generated. Do not edit!


(when (boundp 'custom_behavior_actions::DriveForward)
  (if (not (find-package "CUSTOM_BEHAVIOR_ACTIONS"))
    (make-package "CUSTOM_BEHAVIOR_ACTIONS"))
  (shadow 'DriveForward (find-package "CUSTOM_BEHAVIOR_ACTIONS")))
(unless (find-package "CUSTOM_BEHAVIOR_ACTIONS::DRIVEFORWARD")
  (make-package "CUSTOM_BEHAVIOR_ACTIONS::DRIVEFORWARD"))

(in-package "ROS")
;;//! \htmlinclude DriveForward.msg.html


(defclass custom_behavior_actions::DriveForward
  :super ros::object
  :slots (_distance ))

(defmethod custom_behavior_actions::DriveForward
  (:init
   (&key
    ((:distance __distance) 0.0)
    )
   (send-super :init)
   (setq _distance (float __distance))
   self)
  (:distance
   (&optional __distance)
   (if __distance (setq _distance __distance)) _distance)
  (:serialization-length
   ()
   (+
    ;; float32 _distance
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _distance
       (sys::poke _distance (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _distance
     (setq _distance (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get custom_behavior_actions::DriveForward :md5sum-) "6e77fb10f0c8b4833ec273aa9ac74459")
(setf (get custom_behavior_actions::DriveForward :datatype-) "custom_behavior_actions/DriveForward")
(setf (get custom_behavior_actions::DriveForward :definition-)
      "# Custom message for driving forward
float32 distance    # Distance to drive forward (in meters)


")



(provide :custom_behavior_actions/DriveForward "6e77fb10f0c8b4833ec273aa9ac74459")


