; Auto-generated. Do not edit!


(cl:in-package gazebo_launch-msg)


;//! \htmlinclude DriveForwardResult.msg.html

(cl:defclass <DriveForwardResult> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass DriveForwardResult (<DriveForwardResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DriveForwardResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DriveForwardResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gazebo_launch-msg:<DriveForwardResult> is deprecated: use gazebo_launch-msg:DriveForwardResult instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <DriveForwardResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gazebo_launch-msg:success-val is deprecated.  Use gazebo_launch-msg:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DriveForwardResult>) ostream)
  "Serializes a message object of type '<DriveForwardResult>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DriveForwardResult>) istream)
  "Deserializes a message object of type '<DriveForwardResult>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DriveForwardResult>)))
  "Returns string type for a message object of type '<DriveForwardResult>"
  "gazebo_launch/DriveForwardResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DriveForwardResult)))
  "Returns string type for a message object of type 'DriveForwardResult"
  "gazebo_launch/DriveForwardResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DriveForwardResult>)))
  "Returns md5sum for a message object of type '<DriveForwardResult>"
  "358e233cde0c8a8bcfea4ce193f8fc15")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DriveForwardResult)))
  "Returns md5sum for a message object of type 'DriveForwardResult"
  "358e233cde0c8a8bcfea4ce193f8fc15")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DriveForwardResult>)))
  "Returns full string definition for message of type '<DriveForwardResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#result~%bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DriveForwardResult)))
  "Returns full string definition for message of type 'DriveForwardResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#result~%bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DriveForwardResult>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DriveForwardResult>))
  "Converts a ROS message object to a list"
  (cl:list 'DriveForwardResult
    (cl:cons ':success (success msg))
))
